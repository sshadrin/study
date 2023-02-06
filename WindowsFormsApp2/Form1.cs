using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        public int age, age_1, age_2;
        public string name, name_1;
        public Form1()
        {
            InitializeComponent();
        }
        private void btnClickThis_Click(object sender, EventArgs e)
        {
            name = input1.Text;
            age = Convert.ToInt32(input2.Text);
            age_1 = Convert.ToInt32(input3.Text);

            if (age_1 > age)
            {
                lblages.Text = "Предполагаемый возраст больше возраста " + name + " на " + (age_1 - age) + " лет!";
            }
            else if (age_1 == age)
            {
                lblages.Text = "Возраст сотрудника и предполагаемый равны!";
            }
            else
            {
                lblages.Text = "Возраст " + name + " больше предполагаемого на " + (age - age_1) + " лет!";
            }
        }
        private void btnClickThis1_Click(object sender, EventArgs e)
        {
            name_1 = input4.Text;
            age_2 = Convert.ToInt32(input5.Text);

            if (age_2 < age)
            {
                lblages_1.Text = "Сотрудник 1 старше!";
            }
            else if (age_2 == age)
            {
                lblages_1.Text = "Сотрудники ровесники!";
            }
            else
            {
                lblages_1.Text = "Сотрудник 2 старше!";
            }
        }
    }
}