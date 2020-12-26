
namespace SVData
{
    partial class Main
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Main_Title = new System.Windows.Forms.Label();
            this.Main_Version = new System.Windows.Forms.Label();
            this.Main_CreatedBy = new System.Windows.Forms.Label();
            this.Main_GetData = new System.Windows.Forms.Button();
            this.Main_Search = new System.Windows.Forms.Button();
            this.Main_Compare = new System.Windows.Forms.Button();
            this.Main_Quit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Main_Title
            // 
            this.Main_Title.AutoSize = true;
            this.Main_Title.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.Main_Title.Location = new System.Drawing.Point(349, 62);
            this.Main_Title.Name = "Main_Title";
            this.Main_Title.Size = new System.Drawing.Size(114, 41);
            this.Main_Title.TabIndex = 0;
            this.Main_Title.Text = "SVData";
            this.Main_Title.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // Main_Version
            // 
            this.Main_Version.AutoSize = true;
            this.Main_Version.Location = new System.Drawing.Point(349, 118);
            this.Main_Version.Name = "Main_Version";
            this.Main_Version.Size = new System.Drawing.Size(113, 25);
            this.Main_Version.TabIndex = 1;
            this.Main_Version.Text = "Version 2.0.0";
            this.Main_Version.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // Main_CreatedBy
            // 
            this.Main_CreatedBy.AutoSize = true;
            this.Main_CreatedBy.Location = new System.Drawing.Point(331, 143);
            this.Main_CreatedBy.Name = "Main_CreatedBy";
            this.Main_CreatedBy.Size = new System.Drawing.Size(147, 25);
            this.Main_CreatedBy.TabIndex = 2;
            this.Main_CreatedBy.Text = "Created by Asdia";
            // 
            // Main_GetData
            // 
            this.Main_GetData.Location = new System.Drawing.Point(177, 241);
            this.Main_GetData.Name = "Main_GetData";
            this.Main_GetData.Size = new System.Drawing.Size(112, 34);
            this.Main_GetData.TabIndex = 3;
            this.Main_GetData.Text = "Get Data";
            this.Main_GetData.UseVisualStyleBackColor = true;
            this.Main_GetData.Click += new System.EventHandler(this.Main_GetData_Click);
            // 
            // Main_Search
            // 
            this.Main_Search.Location = new System.Drawing.Point(349, 241);
            this.Main_Search.Name = "Main_Search";
            this.Main_Search.Size = new System.Drawing.Size(112, 34);
            this.Main_Search.TabIndex = 4;
            this.Main_Search.Text = "Search";
            this.Main_Search.UseVisualStyleBackColor = true;
            this.Main_Search.Click += new System.EventHandler(this.Main_Search_Click);
            // 
            // Main_Compare
            // 
            this.Main_Compare.Location = new System.Drawing.Point(521, 241);
            this.Main_Compare.Name = "Main_Compare";
            this.Main_Compare.Size = new System.Drawing.Size(112, 34);
            this.Main_Compare.TabIndex = 5;
            this.Main_Compare.Text = "Compare";
            this.Main_Compare.UseVisualStyleBackColor = true;
            this.Main_Compare.Click += new System.EventHandler(this.Main_Compare_Click);
            // 
            // Main_Quit
            // 
            this.Main_Quit.Location = new System.Drawing.Point(349, 357);
            this.Main_Quit.Name = "Main_Quit";
            this.Main_Quit.Size = new System.Drawing.Size(112, 34);
            this.Main_Quit.TabIndex = 7;
            this.Main_Quit.Text = "Quit";
            this.Main_Quit.UseVisualStyleBackColor = true;
            this.Main_Quit.Click += new System.EventHandler(this.Main_Quit_Click);
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Main_Quit);
            this.Controls.Add(this.Main_Compare);
            this.Controls.Add(this.Main_Search);
            this.Controls.Add(this.Main_GetData);
            this.Controls.Add(this.Main_CreatedBy);
            this.Controls.Add(this.Main_Version);
            this.Controls.Add(this.Main_Title);
            this.Name = "Main";
            this.Text = "SVData: Main";
            this.Icon = new System.Drawing.Icon(@"SVData\icon.ico");
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Main_Quit_Click);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Main_Title;
        private System.Windows.Forms.Label Main_Version;
        private System.Windows.Forms.Label Main_CreatedBy;
        private System.Windows.Forms.Button Main_GetData;
        private System.Windows.Forms.Button Main_Search;
        private System.Windows.Forms.Button Main_Compare;
        private System.Windows.Forms.Button Main_Quit;
    }
}