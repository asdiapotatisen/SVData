
namespace SVData
{
    partial class Search
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
            this.Search_Output = new System.Windows.Forms.TextBox();
            this.Search_label1 = new System.Windows.Forms.Label();
            this.Search_label2 = new System.Windows.Forms.Label();
            this.Search_label3 = new System.Windows.Forms.Label();
            this.Search_Date = new System.Windows.Forms.DateTimePicker();
            this.Search_Answer = new System.Windows.Forms.ComboBox();
            this.Search_Key = new System.Windows.Forms.ComboBox();
            this.Search_Operation = new System.Windows.Forms.ComboBox();
            this.Search_Submit = new System.Windows.Forms.Button();
            this.Search_Save = new System.Windows.Forms.Button();
            this.Search_Cancel = new System.Windows.Forms.Button();
            this.Search_Value = new System.Windows.Forms.TextBox();
            this.Search_removenullvalues = new System.Windows.Forms.RadioButton();
            this.Search_date2 = new System.Windows.Forms.DateTimePicker();
            this.Search_label4 = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.Search_openfile = new System.Windows.Forms.Button();
            this.Search_Range = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // Search_Output
            // 
            this.Search_Output.Location = new System.Drawing.Point(25, 12);
            this.Search_Output.Multiline = true;
            this.Search_Output.Name = "Search_Output";
            this.Search_Output.ReadOnly = true;
            this.Search_Output.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.Search_Output.Size = new System.Drawing.Size(750, 178);
            this.Search_Output.TabIndex = 2;
            // 
            // Search_label1
            // 
            this.Search_label1.AutoSize = true;
            this.Search_label1.Location = new System.Drawing.Point(9, 197);
            this.Search_label1.Name = "Search_label1";
            this.Search_label1.Size = new System.Drawing.Size(64, 25);
            this.Search_label1.TabIndex = 3;
            this.Search_label1.Text = "Search";
            // 
            // Search_label2
            // 
            this.Search_label2.AutoSize = true;
            this.Search_label2.Location = new System.Drawing.Point(440, 197);
            this.Search_label2.Name = "Search_label2";
            this.Search_label2.Size = new System.Drawing.Size(59, 25);
            this.Search_label2.TabIndex = 4;
            this.Search_label2.Text = "where";
            // 
            // Search_label3
            // 
            this.Search_label3.AutoSize = true;
            this.Search_label3.Location = new System.Drawing.Point(433, 238);
            this.Search_label3.Name = "Search_label3";
            this.Search_label3.Size = new System.Drawing.Size(51, 25);
            this.Search_label3.TabIndex = 5;
            this.Search_label3.Text = "from";
            // 
            // Search_Date
            // 
            this.Search_Date.Location = new System.Drawing.Point(490, 235);
            this.Search_Date.Name = "Search_Date";
            this.Search_Date.Size = new System.Drawing.Size(289, 31);
            this.Search_Date.TabIndex = 6;
            // 
            // Search_Answer
            // 
            this.Search_Answer.Items.AddRange(new object[] {
            "api use count",
            "category",
            "comment likes",
            "credits",
            "credits invested",
            "default role id",
            "description",
            "discord ban count",
            "discord commends",
            "discord commends sent",
            "discord game xp",
            "discord id",
            "discord kick count",
            "discord last commend hour",
            "discord last commend message",
            "discord last message minute",
            "discord message count",
            "discord message xp",
            "discord warning count",
            "district",
            "id",
            "image url",
            "minecraft id",
            "name",
            "nationstate",
            "open",
            "owner_id",
            "post likes",
            "twitch id",
            "twitch last message minute",
            "twitch message xp",
            "twitch messages"});
            this.Search_Answer.Location = new System.Drawing.Point(147, 194);
            this.Search_Answer.Name = "Search_Answer";
            this.Search_Answer.Size = new System.Drawing.Size(287, 33);
            this.Search_Answer.TabIndex = 14;
            // 
            // Search_Key
            // 
            this.Search_Key.FormattingEnabled = true;
            this.Search_Key.Items.AddRange(new object[] {
            "api use count",
            "category",
            "comment likes",
            "credits",
            "credits invested",
            "default role id",
            "description",
            "discord ban count",
            "discord commends",
            "discord commends sent",
            "discord game xp",
            "discord id",
            "discord kick count",
            "discord last commend hour",
            "discord last commend message",
            "discord last message minute",
            "discord message count",
            "discord message xp",
            "discord warning count",
            "district",
            "id",
            "image url",
            "minecraft id",
            "name",
            "nationstate",
            "open",
            "owner_id",
            "post likes",
            "twitch id",
            "twitch last message minute",
            "twitch message xp",
            "twitch messages"});
            this.Search_Key.Location = new System.Drawing.Point(505, 194);
            this.Search_Key.Name = "Search_Key";
            this.Search_Key.Size = new System.Drawing.Size(287, 33);
            this.Search_Key.TabIndex = 8;
            // 
            // Search_Operation
            // 
            this.Search_Operation.FormattingEnabled = true;
            this.Search_Operation.Items.AddRange(new object[] {
            "is",
            "is not",
            "contains",
            "greater than",
            "less than"});
            this.Search_Operation.Location = new System.Drawing.Point(19, 235);
            this.Search_Operation.Name = "Search_Operation";
            this.Search_Operation.Size = new System.Drawing.Size(115, 33);
            this.Search_Operation.TabIndex = 9;
            // 
            // Search_Submit
            // 
            this.Search_Submit.Location = new System.Drawing.Point(197, 392);
            this.Search_Submit.Name = "Search_Submit";
            this.Search_Submit.Size = new System.Drawing.Size(112, 34);
            this.Search_Submit.TabIndex = 11;
            this.Search_Submit.Text = "Submit";
            this.Search_Submit.UseVisualStyleBackColor = true;
            this.Search_Submit.Click += new System.EventHandler(this.Search_Submit_Click);
            // 
            // Search_Save
            // 
            this.Search_Save.Location = new System.Drawing.Point(337, 392);
            this.Search_Save.Name = "Search_Save";
            this.Search_Save.Size = new System.Drawing.Size(148, 34);
            this.Search_Save.TabIndex = 12;
            this.Search_Save.Text = "Save results";
            this.Search_Save.UseVisualStyleBackColor = true;
            this.Search_Save.Click += new System.EventHandler(this.Search_Save_Click);
            // 
            // Search_Cancel
            // 
            this.Search_Cancel.Location = new System.Drawing.Point(516, 392);
            this.Search_Cancel.Name = "Search_Cancel";
            this.Search_Cancel.Size = new System.Drawing.Size(112, 34);
            this.Search_Cancel.TabIndex = 13;
            this.Search_Cancel.Text = "Cancel";
            this.Search_Cancel.UseVisualStyleBackColor = true;
            this.Search_Cancel.Click += new System.EventHandler(this.Search_Cancel_Click);
            // 
            // Search_Value
            // 
            this.Search_Value.Location = new System.Drawing.Point(140, 235);
            this.Search_Value.Multiline = true;
            this.Search_Value.Name = "Search_Value";
            this.Search_Value.Size = new System.Drawing.Size(287, 33);
            this.Search_Value.TabIndex = 15;
            // 
            // Search_removenullvalues
            // 
            this.Search_removenullvalues.AutoSize = true;
            this.Search_removenullvalues.Location = new System.Drawing.Point(317, 357);
            this.Search_removenullvalues.Name = "Search_removenullvalues";
            this.Search_removenullvalues.Size = new System.Drawing.Size(188, 29);
            this.Search_removenullvalues.TabIndex = 16;
            this.Search_removenullvalues.TabStop = true;
            this.Search_removenullvalues.Text = "Remove null values";
            this.Search_removenullvalues.UseVisualStyleBackColor = true;
            // 
            // Search_date2
            // 
            this.Search_date2.Location = new System.Drawing.Point(281, 274);
            this.Search_date2.Name = "Search_date2";
            this.Search_date2.Size = new System.Drawing.Size(289, 31);
            this.Search_date2.TabIndex = 17;
            // 
            // Search_label4
            // 
            this.Search_label4.AutoSize = true;
            this.Search_label4.Location = new System.Drawing.Point(246, 274);
            this.Search_label4.Name = "Search_label4";
            this.Search_label4.Size = new System.Drawing.Size(29, 25);
            this.Search_label4.TabIndex = 18;
            this.Search_label4.Text = "to";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // Search_openfile
            // 
            this.Search_openfile.Location = new System.Drawing.Point(317, 317);
            this.Search_openfile.Name = "Search_openfile";
            this.Search_openfile.Size = new System.Drawing.Size(182, 34);
            this.Search_openfile.TabIndex = 19;
            this.Search_openfile.Text = "Input file";
            this.Search_openfile.UseVisualStyleBackColor = true;
            this.Search_openfile.Visible = false;
            this.Search_openfile.Click += new System.EventHandler(this.Search_openfile_Click);
            // 
            // Search_Range
            // 
            this.Search_Range.FormattingEnabled = true;
            this.Search_Range.Items.AddRange(new object[] {
            "all",
            "file"});
            this.Search_Range.Location = new System.Drawing.Point(79, 194);
            this.Search_Range.Name = "Search_Range";
            this.Search_Range.Size = new System.Drawing.Size(62, 33);
            this.Search_Range.TabIndex = 20;
            this.Search_Range.SelectedIndexChanged += new System.EventHandler(this.Search_Range_SelectedIndexChanged);
            // 
            // Search
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Search_Range);
            this.Controls.Add(this.Search_openfile);
            this.Controls.Add(this.Search_label4);
            this.Controls.Add(this.Search_date2);
            this.Controls.Add(this.Search_removenullvalues);
            this.Controls.Add(this.Search_Value);
            this.Controls.Add(this.Search_Cancel);
            this.Controls.Add(this.Search_Save);
            this.Controls.Add(this.Search_Submit);
            this.Controls.Add(this.Search_Operation);
            this.Controls.Add(this.Search_Key);
            this.Controls.Add(this.Search_Answer);
            this.Controls.Add(this.Search_Date);
            this.Controls.Add(this.Search_label3);
            this.Controls.Add(this.Search_label2);
            this.Controls.Add(this.Search_label1);
            this.Controls.Add(this.Search_Output);
            this.Name = "Search";
            this.Text = "SVData: Search";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.TextBox Search_Output;
        private System.Windows.Forms.Label Search_label1;
        private System.Windows.Forms.Label Search_label2;
        private System.Windows.Forms.Label Search_label3;
        private System.Windows.Forms.DateTimePicker Search_Date;
        private System.Windows.Forms.ComboBox Search_Answer;
        private System.Windows.Forms.ComboBox Search_Key;
        private System.Windows.Forms.ComboBox Search_Operation;
        private System.Windows.Forms.Button Search_Submit;
        private System.Windows.Forms.Button Search_Save;
        private System.Windows.Forms.Button Search_Cancel;
        private System.Windows.Forms.TextBox Search_Value;
        private System.Windows.Forms.RadioButton Search_removenullvalues;
        private System.Windows.Forms.DateTimePicker Search_date2;
        private System.Windows.Forms.Label Search_label4;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button Search_openfile;
        private System.Windows.Forms.ComboBox Search_Range;
    }
}