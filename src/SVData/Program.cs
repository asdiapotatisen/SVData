using System;
using System.Windows.Forms;

namespace SVData
{
    static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Console.WriteLine("Hey!");
            Application.Run(new Main());
            Console.WriteLine("You should see a window now.");
        }
    }
}
