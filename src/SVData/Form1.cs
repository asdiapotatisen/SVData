using System;
using System.Windows.Forms;

namespace SVData
{
    public partial class Main : Form
    {
        public Main()
        {
            InitializeComponent();
        }

        private void Main_GetData_Click(object sender, EventArgs e)
        {
            var GetDataWindow = new GetData();
            GetDataWindow.Show();
            this.Hide();
        }
        private void Main_Search_Click(object sender, EventArgs e)
        {
            var SearchWindow = new Search();
            SearchWindow.Show();
            this.Hide();
        }
        private void Main_Compare_Click(object sender, EventArgs e)
        {
            var CompareWindow = new Compare();
            CompareWindow.Show();
            this.Hide();
        }
        private void Main_Quit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
