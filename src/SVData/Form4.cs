using System;
using System.Collections.Generic;
using System.IO;
using System.Windows.Forms;
using Newtonsoft.Json;
using System.Linq;

namespace SVData
{
    public partial class Compare : Form
    {
        public string filePath1;
        public string filePath2;
        List<dynamic> answerlist = new List<dynamic>();

        public Compare()
        {
            InitializeComponent();
        }

        private void Compare_Cancel_Click(object sender, EventArgs e)
        {
            this.Close();
            var MainWindow = new Main();
            MainWindow.Show();
        }

        private void Compare_Save_Click(object sender, EventArgs e)
        {
            FileStream myStream;
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();

            saveFileDialog1.Filter = "txt files (*.txt)|*.txt";
            saveFileDialog1.FilterIndex = 2;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Path.GetDirectoryName(Application.StartupPath) + @"\SVData\Results\Compare";

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if ((myStream = (FileStream)saveFileDialog1.OpenFile()) != null)
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

        private void Compare_Submit_Click(object sender, EventArgs e)
        {
            Compare_Output.Clear();
            Compare_Output.Text = "Comparing...";
            string mode = Compare_Mode.Text;

            if (mode == "AND")
            {
                List<dynamic> list1 = new List<dynamic>();
                List<dynamic> list2 = new List<dynamic>();

                try
                {
                    var text1 = File.ReadAllText(filePath1);
                    list1 = JsonConvert.DeserializeObject<List<dynamic>>(text1);
                }
                catch { }

                try
                {
                    var text2 = File.ReadAllText(filePath2);
                    list2 = JsonConvert.DeserializeObject<List<dynamic>>(text2);
                }
                catch { }


                foreach (var item1 in list1)
                {
                    foreach (var item2 in list2)
                    {
                        if (item1 == item2)
                        {
                            answerlist.Add(item1);
                        }
                    }
                }
            }
            else if (mode == "XOR")
            {
                List<dynamic> list1 = new List<dynamic>();
                List<dynamic> list2 = new List<dynamic>();

                try
                {
                    var text1 = File.ReadAllText(filePath1);
                    list1 = JsonConvert.DeserializeObject<List<dynamic>>(text1);
                }
                catch { }

                try
                {
                    var text2 = File.ReadAllText(filePath2);
                    list2 = JsonConvert.DeserializeObject<List<dynamic>>(text2);
                }
                catch { }

                // get items that are in both lists
                List<dynamic> inbothlists = new List<dynamic>();

                foreach (var item1 in list1)
                {
                    foreach (var item2 in list2)
                    {
                        if (item1 == item2)
                        {
                            inbothlists.Add(item1);
                        }
                    }
                }

                list1.AddRange(list2);

                // get all items
                answerlist = list1.Distinct().ToList();

                // remove items that are in both lists
                foreach (var item in inbothlists)
                {
                    answerlist.Remove(item);
                }
            }
            else if (mode == "OR")
            {
                List<dynamic> list1 = new List<dynamic>();
                List<dynamic> list2 = new List<dynamic>();

                try
                {
                    var text1 = File.ReadAllText(filePath1);
                    list1 = JsonConvert.DeserializeObject<List<dynamic>>(text1);
                }
                catch { }

                try
                {
                    var text2 = File.ReadAllText(filePath2);
                    list2 = JsonConvert.DeserializeObject<List<dynamic>>(text2);
                }
                catch { }

                list1.AddRange(list2);

                answerlist = list1.Distinct().ToList();
            }

            Compare_Output.Clear();
            if (answerlist.Count == 0)
            {
                Compare_Output.Text = "No results were found.";
                Compare_Save.Enabled = false;
            }

            else
            {
                Compare_Save.Enabled = true;
                foreach (var item in answerlist)
                {
                    Compare_Output.AppendText(item.ToString());
                    Compare_Output.AppendText(Environment.NewLine);
                }
                Compare_Output.AppendText(answerlist.Count.ToString());
                Compare_Output.AppendText(" results were found.");
            }

        }
        private void Compare_In1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "txt files (*.txt)|*.txt";
            openFileDialog1.FilterIndex = 2;
            openFileDialog1.InitialDirectory = Path.GetDirectoryName(Application.StartupPath) + @"\SVData\Results";
            openFileDialog1.FileName = "";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                filePath1 = openFileDialog1.FileName;
            }
            Compare_In1.Text = Path.GetFileNameWithoutExtension(filePath1);
        }

        private void Compare_In2_Click(object sender, EventArgs e)
        {
            openFileDialog2.Filter = "txt files (*.txt)|*.txt";
            openFileDialog2.FilterIndex = 2;
            openFileDialog2.FileName = "";
            openFileDialog2.InitialDirectory = Path.GetDirectoryName(Application.StartupPath) + @"\SVData\Results";
            if (openFileDialog2.ShowDialog() == DialogResult.OK)
            {
                filePath2 = openFileDialog2.FileName;
            }
            Compare_In2.Text = Path.GetFileNameWithoutExtension(filePath2);
        }
    }
}
