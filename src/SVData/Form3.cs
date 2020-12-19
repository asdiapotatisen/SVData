using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
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
            Search_Output.Text = "";
            Search_Output.AppendText("Searching...");
            string answerkey = Search_Answer.Text;
            string key = Search_Key.Text;
            string operation = Search_Operation.Text;
            string value = Search_Value.Text;
            string date = Search_Date.Value.ToString("dd-MM-yy");

            answerlist.Clear();
            var text = File.ReadAllText("SVData/database.json");
            Dictionary<string, Dictionary<string, Dictionary<string, dynamic>>> database = JsonConvert.DeserializeObject<Dictionary<string, Dictionary<string, Dictionary<string, dynamic>>>>(text);
            foreach (string svid in database.Keys)
            {
                if (operation == "is")
                {
                    try
                    {
                        if (database[svid][date][key] == value)
                        {
                            dynamic answervalue = database[svid][date][answerkey];
                            answerlist.Add(answervalue);
                        }
                    }
                    catch
                    {}
                }
                if (operation == "is not")
                {
                    try
                    {
                        if (database[svid][date][key] != value)
                        {
                            dynamic answervalue = database[svid][date][answerkey];
                            answerlist.Add(answervalue);
                        }
                    }
                    catch
                    {}
                }
                if (operation == "contains")
                {
                    try
                    {
                        if (database[svid][date][key].ToString().Contains(value))
                        {
                            dynamic answervalue = database[svid][date][answerkey];
                            answerlist.Add(answervalue);
                        }
                    }
                    catch
                    {}
                }
                if (operation == "less than")
                {
                    try
                    {
                        if (database[svid][date][key] <= Int64.Parse(value))
                        {
                            dynamic answervalue = database[svid][date][answerkey];
                            answerlist.Add(answervalue);
                        }
                    }
                    catch
                    {}
                }
                if (operation == "greater than")
                {
                    try
                    {
                        if (database[svid][date][key] >= Int64.Parse(value))
                        {
                            dynamic answervalue = database[svid][date][answerkey];
                            answerlist.Add(answervalue);
                        }
                    }
                    catch
                    {}
                }
                if (operation == "equals to")
                {
                    try
                    {
                        if (database[svid][date][key] == Int64.Parse(value))
                        {
                            dynamic answervalue = database[svid][date][answerkey];
                            answerlist.Add(answervalue);
                        }
                    }
                    catch
                    { }
                }
            }
            Search_Output.Text = "";
            if (answerlist.Count == 0)
            {
                Search_Output.Text = "No results were found.";
            }
            else
            {
                foreach (var item in answerlist)
                {
                    if (item is not null)
                    {
                        Search_Output.AppendText(item.ToString());
                        Search_Output.AppendText(Environment.NewLine);
                    }
                }
            }
        }
        public void Search_Save_Click(object sender, EventArgs e)
        {
            FileStream myStream;
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();

            saveFileDialog1.Filter = "txt files (*.txt)|*.txt";
            saveFileDialog1.FilterIndex = 2;
            saveFileDialog1.RestoreDirectory = true;

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
