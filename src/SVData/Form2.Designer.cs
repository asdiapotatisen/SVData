
namespace SVData
{
    partial class GetData
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.GetData_GetData = new System.Windows.Forms.Button();
            this.GetData_Cancel = new System.Windows.Forms.Button();
            this.GetData_Progress = new System.Windows.Forms.ProgressBar();
            this.GetData_Status = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // GetData_GetData
            // 
            this.GetData_GetData.Location = new System.Drawing.Point(272, 359);
            this.GetData_GetData.Name = "GetData_GetData";
            this.GetData_GetData.Size = new System.Drawing.Size(112, 34);
            this.GetData_GetData.TabIndex = 0;
            this.GetData_GetData.Text = "Get Data";
            this.GetData_GetData.UseVisualStyleBackColor = true;
            this.GetData_GetData.Click += new System.EventHandler(this.GetData_GetData_Click);
            // 
            // GetData_Cancel
            // 
            this.GetData_Cancel.Location = new System.Drawing.Point(432, 359);
            this.GetData_Cancel.Name = "GetData_Cancel";
            this.GetData_Cancel.Size = new System.Drawing.Size(112, 34);
            this.GetData_Cancel.TabIndex = 1;
            this.GetData_Cancel.Text = "Cancel";
            this.GetData_Cancel.UseVisualStyleBackColor = true;
            this.GetData_Cancel.Click += new System.EventHandler(this.GetData_Cancel_Click);
            // 
            // GetData_Progress
            // 
            this.GetData_Progress.Location = new System.Drawing.Point(98, 109);
            this.GetData_Progress.Name = "GetData_Progress";
            this.GetData_Progress.Size = new System.Drawing.Size(621, 41);
            this.GetData_Progress.TabIndex = 4;
            // 
            // GetData_Status
            // 
            this.GetData_Status.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.GetData_Status.AutoSize = true;
            this.GetData_Status.Location = new System.Drawing.Point(335, 225);
            this.GetData_Status.Name = "GetData_Status";
            this.GetData_Status.Size = new System.Drawing.Size(149, 25);
            this.GetData_Status.TabIndex = 5;
            this.GetData_Status.Text = "        Idling...        ";
            this.GetData_Status.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // GetData
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.GetData_Status);
            this.Controls.Add(this.GetData_Progress);
            this.Controls.Add(this.GetData_Cancel);
            this.Controls.Add(this.GetData_GetData);
            this.Name = "GetData";
            this.Text = "SVData: Get Data";
            this.ResumeLayout(false);
            this.PerformLayout();
            this.Icon = new System.Drawing.Icon(@"SVData\icon.ico");

        }

        #endregion

        private System.Windows.Forms.Button GetData_GetData;
        private System.Windows.Forms.Button GetData_Cancel;
        private System.Windows.Forms.ProgressBar GetData_Progress;
        private System.Windows.Forms.Label GetData_Status;
    }
}