using System;

namespace WindowsFormsApp2
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnClickThis = new System.Windows.Forms.Button();
            this.lblages = new System.Windows.Forms.Label();
            this.input1 = new System.Windows.Forms.TextBox();
            this.input2 = new System.Windows.Forms.TextBox();
            this.input3 = new System.Windows.Forms.TextBox();
            this.btnClickThis1 = new System.Windows.Forms.Button();
            this.input4 = new System.Windows.Forms.TextBox();
            this.input5 = new System.Windows.Forms.TextBox();
            this.lblages_1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnClickThis
            // 
            this.btnClickThis.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.btnClickThis.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.btnClickThis.Location = new System.Drawing.Point(239, 125);
            this.btnClickThis.Name = "btnClickThis";
            this.btnClickThis.Size = new System.Drawing.Size(197, 53);
            this.btnClickThis.TabIndex = 0;
            this.btnClickThis.Text = "Сравнить предполагаемый возраст и возраст сотрудника";
            this.btnClickThis.UseVisualStyleBackColor = false;
            this.btnClickThis.Click += new System.EventHandler(this.btnClickThis_Click);
            // 
            // lblages
            // 
            this.lblages.AutoSize = true;
            this.lblages.BackColor = System.Drawing.Color.Cyan;
            this.lblages.ForeColor = System.Drawing.Color.Black;
            this.lblages.Location = new System.Drawing.Point(161, 89);
            this.lblages.Name = "lblages";
            this.lblages.Size = new System.Drawing.Size(39, 13);
            this.lblages.TabIndex = 1;
            this.lblages.Text = "Output";
            // 
            // input1
            // 
            this.input1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.input1.Location = new System.Drawing.Point(0, 27);
            this.input1.Name = "input1";
            this.input1.Size = new System.Drawing.Size(200, 20);
            this.input1.TabIndex = 2;
            this.input1.Text = "Enter name";
            this.input1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // input2
            // 
            this.input2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.input2.Location = new System.Drawing.Point(239, 27);
            this.input2.Name = "input2";
            this.input2.Size = new System.Drawing.Size(241, 20);
            this.input2.TabIndex = 3;
            this.input2.Text = "Enter age";
            this.input2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // input3
            // 
            this.input3.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.input3.Location = new System.Drawing.Point(516, 27);
            this.input3.Name = "input3";
            this.input3.Size = new System.Drawing.Size(244, 20);
            this.input3.TabIndex = 4;
            this.input3.Text = "Estimated age";
            this.input3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // btnClickThis1
            // 
            this.btnClickThis1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.btnClickThis1.ForeColor = System.Drawing.Color.White;
            this.btnClickThis1.Location = new System.Drawing.Point(217, 397);
            this.btnClickThis1.Name = "btnClickThis1";
            this.btnClickThis1.Size = new System.Drawing.Size(219, 41);
            this.btnClickThis1.TabIndex = 5;
            this.btnClickThis1.Text = "Сравнить возраст первого сотрудника и второго";
            this.btnClickThis1.UseVisualStyleBackColor = false;
            this.btnClickThis1.Click += new System.EventHandler(this.btnClickThis1_Click);
            // 
            // input4
            // 
            this.input4.BackColor = System.Drawing.Color.Blue;
            this.input4.ForeColor = System.Drawing.Color.White;
            this.input4.Location = new System.Drawing.Point(0, 299);
            this.input4.Name = "input4";
            this.input4.Size = new System.Drawing.Size(200, 20);
            this.input4.TabIndex = 6;
            this.input4.Text = "Enter second name";
            this.input4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // input5
            // 
            this.input5.BackColor = System.Drawing.Color.Blue;
            this.input5.ForeColor = System.Drawing.Color.White;
            this.input5.Location = new System.Drawing.Point(239, 299);
            this.input5.Name = "input5";
            this.input5.Size = new System.Drawing.Size(241, 20);
            this.input5.TabIndex = 0;
            this.input5.Text = "Enter second age";
            this.input5.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lblages_1
            // 
            this.lblages_1.AutoSize = true;
            this.lblages_1.BackColor = System.Drawing.Color.Cyan;
            this.lblages_1.Location = new System.Drawing.Point(164, 354);
            this.lblages_1.Name = "lblages_1";
            this.lblages_1.Size = new System.Drawing.Size(39, 13);
            this.lblages_1.TabIndex = 7;
            this.lblages_1.Text = "Output";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(763, 453);
            this.Controls.Add(this.lblages_1);
            this.Controls.Add(this.input5);
            this.Controls.Add(this.input4);
            this.Controls.Add(this.btnClickThis1);
            this.Controls.Add(this.input3);
            this.Controls.Add(this.input2);
            this.Controls.Add(this.input1);
            this.Controls.Add(this.lblages);
            this.Controls.Add(this.btnClickThis);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnClickThis;
        private System.Windows.Forms.Label lblages;
        private System.Windows.Forms.TextBox input1;
        private System.Windows.Forms.TextBox input2;
        private System.Windows.Forms.TextBox input3;
        private System.Windows.Forms.Button btnClickThis1;
        private System.Windows.Forms.TextBox input4;
        private System.Windows.Forms.TextBox input5;
        private System.Windows.Forms.Label lblages_1;

        public EventHandler Form1_Load { get; private set; }
    }
}

