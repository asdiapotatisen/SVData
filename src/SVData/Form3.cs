using System;
using System.Collections.Generic;
using System.IO;
using System.Windows.Forms;
using Newtonsoft.Json;

namespace SVData
{
    public partial class Search : Form
    {
        public Search()
        {
            InitializeComponent();
        }
        List<dynamic> answerlist = new List<dynamic>();
        public void Search_Submit_Click(object sender, EventArgs e)
        {
            Search_Output.Clear();
            Search_Output.AppendText("Searching...");
            string answerkey = Search_Answer.Text;
            string key = Search_Key.Text;
            string operation = Search_Operation.Text;
            string value = Search_Value.Text;
            DateTime fromdate = Search_Date.Value;
            DateTime todate = Search_date2.Value;
            bool removenull = Search_removenullvalues.Checked;

            if (value == "null")
            {
                value = "";
            }
            answerlist.Clear();
            var text = File.ReadAllText("SVData/database.json");
            Dictionary<string, Dictionary<string, Dictionary<string, dynamic>>> database = JsonConvert.DeserializeObject<Dictionary<string, Dictionary<string, Dictionary<string, dynamic>>>>(text);

            var dateArr = new List<string>();

            for (var date = fromdate; date <= todate.AddDays(1); date = date.AddDays(1))
            {
                dateArr.Add(date.ToString("dd-MM-yy"));
            }

            Search_label1.Text = dateArr.Count.ToString();

            foreach (string svid in database.Keys)
            {
                foreach (string date in dateArr)
                {
                    try
                    {
                        var dbvalue = database[svid][date][key] ?? "";
                        dynamic answervalue = database[svid][date][answerkey] ?? "null";
                        if (operation == "is")
                        {
                            try
                            {
                                if (dbvalue.ToString() == value)
                                {
                                    answerlist.Add(answervalue);
                                }
                            }
                            catch
                            { }
                        }
                        if (operation == "is not")
                        {
                            try
                            {
                                if (dbvalue.ToString() != value)
                                {
                                    answerlist.Add(answervalue);
                                }
                            }
                            catch
                            { }
                        }
                        if (operation == "contains")
                        {
                            try
                            {
                                if (dbvalue.ToString().Contains(value))
                                {
                                    answerlist.Add(answervalue);
                                }
                            }
                            catch
                            { }
                        }
                        if (operation == "less than")
                        {
                            try
                            {
                                if (dbvalue <= Int64.Parse(value))
                                {
                                    answerlist.Add(answervalue);
                                }
                            }
                            catch
                            { }
                        }
                        if (operation == "greater than")
                        {
                            try
                            {
                                if (dbvalue >= Int64.Parse(value))
                                {
                                    answerlist.Add(answervalue);
                                }
                            }
                            catch
                            { }
                        }
                    }
                    catch
                    { }
                }
            }

            List<dynamic> removeditems = new List<dynamic>();
            foreach (var item in answerlist)
            {
                if (removenull == true)
                {
                    if (item.ToString() == "null")
                    {
                        removeditems.Add(item);
                    }
                }
            }

            foreach (var item in removeditems)
            {
                answerlist.Remove(item);
            }

            Search_Output.Text = "";

            if (answerlist.Count == 0)
            {
                Search_Output.Text = "No results were found.";
                Search_Save.Enabled = false;
            }

            else
            {
                Search_Save.Enabled = true;
                foreach (var item in answerlist)
                {
                    Search_Output.AppendText(item.ToString());
                    Search_Output.AppendText(Environment.NewLine);
                }
                Search_Output.AppendText(answerlist.Count.ToString());
                Search_Output.AppendText(" results were found.");
            }
        }
        public void Search_Save_Click(object sender, EventArgs e)
        {
            FileStream myStream;
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();

            saveFileDialog1.Filter = "txt files (*.txt)|*.txt";
            saveFileDialog1.FilterIndex = 2;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Path.GetDirectoryName(Application.StartupPath) + @"\SVData\Results\Search";

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if ((myStream = (FileStream) saveFileDialog1.OpenFile()) != null)
                {
                    myStream.Close();
                    string json = JsonConvert.SerializeObject(answerlist, Formatting.Indented);
                    using (StreamWriter outputFile = new StreamWriter(myStream.Name))
                    {
                        outputFile.Write(json);
                    }
                }
            }
        }

        private void Search_Cancel_Click(object sender, EventArgs e)
        {
            this.Close();
            var MainWindow = new Main();
            MainWindow.Show();
        }
    }
}
