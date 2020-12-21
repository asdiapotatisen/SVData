
namespace SVData
{
    partial class Compare
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
            this.Compare_Output = new System.Windows.Forms.TextBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.openFileDialog2 = new System.Windows.Forms.OpenFileDialog();
            this.Compare_In1 = new System.Windows.Forms.Button();
            this.Compare_In2 = new System.Windows.Forms.Button();
            this.Compare_Mode = new System.Windows.Forms.ComboBox();
            this.Compare_Cancel = new System.Windows.Forms.Button();
            this.Compare_Save = new System.Windows.Forms.Button();
            this.Compare_Submit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Compare_Output
            // 
            this.Compare_Output.Location = new System.Drawing.Point(9, 16);
            this.Compare_Output.Multiline = true;
            this.Compare_Output.Name = "Compare_Output";
            this.Compare_Output.ReadOnly = true;
            this.Compare_Output.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.Compare_Output.Size = new System.Drawing.Size(779, 310);
            this.Compare_Output.TabIndex = 0;
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // openFileDialog2
            // 
            this.openFileDialog2.FileName = "openFileDialog1";
            // 
            // Compare_In1
            // 
            this.Compare_In1.Location = new System.Drawing.Point(234, 348);
            this.Compare_In1.Name = "Compare_In1";
            this.Compare_In1.Size = new System.Drawing.Size(112, 34);
            this.Compare_In1.TabIndex = 1;
            this.Compare_In1.Text = "Input file 1";
            this.Compare_In1.UseVisualStyleBackColor = true;
            this.Compare_In1.Click += new System.EventHandler(this.Compare_In1_Click);
            // 
            // Compare_In2
            // 
            this.Compare_In2.Location = new System.Drawing.Point(422, 348);
            this.Compare_In2.Name = "Compare_In2";
            this.Compare_In2.Size = new System.Drawing.Size(112, 34);
            this.Compare_In2.TabIndex = 2;
            this.Compare_In2.Text = "Input file 2";
            this.Compare_In2.UseVisualStyleBackColor = true;
            this.Compare_In2.Click += new System.EventHandler(this.Compare_In2_Click);
            // 
            // Compare_Mode
            // 
            this.Compare_Mode.FormattingEnabled = true;
            this.Compare_Mode.Location = new System.Drawing.Point(352, 350);
            this.Compare_Mode.Name = "Compare_Mode";
            this.Compare_Mode.Size = new System.Drawing.Size(64, 33);
            this.Compare_Mode.TabIndex = 3;
            this.Compare_Mode.Items.AddRange(new object[] {
                "AND",
                "OR",
                "XOR" });
            // 
            // Compare_Cancel
            // 
            this.Compare_Cancel.Location = new System.Drawing.Point(496, 389);
            this.Compare_Cancel.Name = "Compare_Cancel";
            this.Compare_Cancel.Size = new System.Drawing.Size(112, 34);
            this.Compare_Cancel.TabIndex = 19;
            this.Compare_Cancel.Text = "Cancel";
            this.Compare_Cancel.UseVisualStyleBackColor = true;
            this.Compare_Cancel.Click += new System.EventHandler(this.Compare_Cancel_Click);
            // 
            // Compare_Save
            // 
            this.Compare_Save.Location = new System.Drawing.Point(317, 389);
            this.Compare_Save.Name = "Compare_Save";
            this.Compare_Save.Size = new System.Drawing.Size(148, 34);
            this.Compare_Save.TabIndex = 18;
            this.Compare_Save.Text = "Save results";
            this.Compare_Save.UseVisualStyleBackColor = true;
            this.Compare_Save.Click += new System.EventHandler(this.Compare_Save_Click);
            // 
            // Compare_Submit
            // 
            this.Compare_Submit.Location = new System.Drawing.Point(177, 389);
            this.Compare_Submit.Name = "Compare_Submit";
            this.Compare_Submit.Size = new System.Drawing.Size(112, 34);
            this.Compare_Submit.TabIndex = 17;
            this.Compare_Submit.Text = "Submit";
            this.Compare_Submit.UseVisualStyleBackColor = true;
            this.Compare_Submit.Click += new System.EventHandler(this.Compare_Submit_Click);
            // 
            // Compare
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Compare_Cancel);
            this.Controls.Add(this.Compare_Save);
            this.Controls.Add(this.Compare_Submit);
            this.Controls.Add(this.Compare_Mode);
            this.Controls.Add(this.Compare_In2);
            this.Controls.Add(this.Compare_In1);
            this.Controls.Add(this.Compare_Output);
            this.Name = "Compare";
            this.Icon = new System.Drawing.Icon(@"SVData\icon.ico");
            this.Text = "SVData: Compare";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox Compare_Output;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.OpenFileDialog openFileDialog2;
        private System.Windows.Forms.Button Compare_In1;
        private System.Windows.Forms.Button Compare_In2;
        private System.Windows.Forms.ComboBox Compare_Mode;
        private System.Windows.Forms.Button Compare_Cancel;
        private System.Windows.Forms.Button Compare_Save;
        private System.Windows.Forms.Button Compare_Submit;
    }
}