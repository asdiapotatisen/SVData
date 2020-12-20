
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
            this.Search_Title = new System.Windows.Forms.Label();
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
            this.SuspendLayout();
            // 
            // Search_Title
            // 
            this.Search_Title.AutoSize = true;
            this.Search_Title.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.Search_Title.Location = new System.Drawing.Point(356, 26);
            this.Search_Title.Name = "Search_Title";
            this.Search_Title.Size = new System.Drawing.Size(106, 41);
            this.Search_Title.TabIndex = 1;
            this.Search_Title.Text = "Search";
            this.Search_Title.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // Search_Output
            // 
            this.Search_Output.Location = new System.Drawing.Point(25, 82);
            this.Search_Output.Multiline = true;
            this.Search_Output.Name = "Search_Output";
            this.Search_Output.Size = new System.Drawing.Size(750, 178);
            this.Search_Output.TabIndex = 2;
            this.Search_Output.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            // 
            // Search_label1
            // 
            this.Search_label1.AutoSize = true;
            this.Search_label1.Location = new System.Drawing.Point(33, 280);
            this.Search_label1.Name = "Search_label1";
            this.Search_label1.Size = new System.Drawing.Size(86, 25);
            this.Search_label1.TabIndex = 3;
            this.Search_label1.Text = "Search all";
            // 
            // Search_label2
            // 
            this.Search_label2.AutoSize = true;
            this.Search_label2.Location = new System.Drawing.Point(418, 280);
            this.Search_label2.Name = "Search_label2";
            this.Search_label2.Size = new System.Drawing.Size(59, 25);
            this.Search_label2.TabIndex = 4;
            this.Search_label2.Text = "where";
            // 
            // Search_label3
            // 
            this.Search_label3.AutoSize = true;
            this.Search_label3.Location = new System.Drawing.Point(444, 329);
            this.Search_label3.Name = "Search_label3";
            this.Search_label3.Size = new System.Drawing.Size(33, 25);
            this.Search_label3.TabIndex = 5;
            this.Search_label3.Text = "on";
            // 
            // Search_Date
            // 
            this.Search_Date.Location = new System.Drawing.Point(483, 326);
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
            this.Search_Answer.Location = new System.Drawing.Point(125, 277);
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
            this.Search_Key.Location = new System.Drawing.Point(480, 277);
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
            this.Search_Operation.Location = new System.Drawing.Point(30, 326);
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
            this.Search_Value.Location = new System.Drawing.Point(151, 326);
            this.Search_Value.Multiline = true;
            this.Search_Value.Name = "Search_Value";
            this.Search_Value.Size = new System.Drawing.Size(287, 33);
            this.Search_Value.TabIndex = 15;
            // 
            // Search
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
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
            this.Controls.Add(this.Search_Title);
            this.Name = "Search";
            this.Text = "SVData: Search";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Search_Title;
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
    }
}