# Generated by Django 3.2.3 on 2021-06-30 14:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20210620_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Corderbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_Number', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 190602))),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('CNIC', models.CharField(max_length=30)),
                ('Mobile_Number', models.CharField(max_length=30)),
                ('Whatsapp_Number', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 189603))),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('job_name', models.CharField(max_length=30)),
                ('Hiring_date', models.CharField(max_length=30)),
                ('Employement_year', models.CharField(max_length=30)),
                ('Salary', models.CharField(max_length=30)),
                ('Bonus', models.CharField(max_length=30)),
                ('Account_number', models.CharField(max_length=30)),
                ('Growth', models.CharField(max_length=30)),
                ('Duty_Start_time', models.CharField(max_length=30)),
                ('Duty_End_time', models.CharField(max_length=30)),
                ('Total_hours', models.CharField(max_length=30)),
                ('leaves_allows', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Remarks', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 181607))),
            ],
        ),
        migrations.CreateModel(
            name='indeximg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image1', models.ImageField(upload_to='images')),
                ('product_text1', models.CharField(max_length=100)),
                ('product_desc1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ourdesigns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image1', models.ImageField(upload_to='images')),
                ('product_text1', models.CharField(max_length=100)),
                ('product_desc1', models.CharField(max_length=100)),
                ('product_image2', models.ImageField(upload_to='images')),
                ('product_text2', models.CharField(max_length=100)),
                ('product_desc2', models.CharField(max_length=100)),
                ('product_image3', models.ImageField(upload_to='images')),
                ('product_text3', models.CharField(max_length=100)),
                ('product_desc3', models.CharField(max_length=100)),
                ('product_image4', models.ImageField(upload_to='images')),
                ('product_text4', models.CharField(max_length=100)),
                ('product_desc4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Quality', models.CharField(max_length=30)),
                ('Unit_Price', models.CharField(max_length=30)),
                ('Size', models.CharField(max_length=30)),
                ('Color', models.CharField(max_length=30)),
                ('Division', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Re_Order_Level', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 186604))),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Product_type', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 184606))),
            ],
        ),
        migrations.CreateModel(
            name='productimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='S_Order_Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_Number', models.CharField(max_length=30)),
                ('Total_Bill', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 187604))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='serviceimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='images')),
                ('product_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Organization_Name', models.CharField(max_length=30)),
                ('ISO_Certification', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 185605))),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_name', models.CharField(max_length=30)),
                ('Organization', models.CharField(max_length=30)),
                ('Certification', models.CharField(max_length=30)),
                ('Duty_Start_time', models.TimeField(verbose_name='')),
                ('Duty_End_time', models.TimeField(verbose_name='')),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 183606))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='S_Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Medium', models.CharField(max_length=30)),
                ('Payment_Amount', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 188603))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
                ('S_Order_Booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.s_order_booking')),
            ],
        ),
        migrations.CreateModel(
            name='S_Order_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=30)),
                ('Unit_Price', models.CharField(max_length=30)),
                ('Bulk_Price', models.CharField(max_length=30)),
                ('Packing_Details', models.CharField(max_length=30)),
                ('Unit_sales_Price', models.CharField(max_length=30)),
                ('Bulk_sales_Price', models.CharField(max_length=30)),
                ('Discount', models.CharField(max_length=30)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('S_Order_Booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.s_order_booking')),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='s_order_booking',
            name='Supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier'),
        ),
        migrations.CreateModel(
            name='S_Contact_Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Mobile_Number1', models.CharField(max_length=30)),
                ('Mobile_Number2', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 189603))),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='S_Contact_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Toll_free_Number', models.CharField(max_length=30)),
                ('LandLine_Number', models.CharField(max_length=30)),
                ('Mobile_Number1', models.CharField(max_length=30)),
                ('Mobile_Number2', models.CharField(max_length=30)),
                ('Postal_Code', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 188603))),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=30)),
                ('Years_of_Passing', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=2)),
                ('Institute', models.CharField(max_length=30)),
                ('Total_Marks', models.CharField(max_length=30)),
                ('Obtain_Marks', models.CharField(max_length=30)),
                ('Grade', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 182606))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Size_Available', models.CharField(max_length=30)),
                ('Color_Available', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 185605))),
                ('Product_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_category')),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_type'),
        ),
        migrations.AddField(
            model_name='product',
            name='Supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier'),
        ),
        migrations.CreateModel(
            name='Previous_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Previous_Organization', models.CharField(max_length=30)),
                ('Job_Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Duty_Start_time', models.TimeField(verbose_name='')),
                ('Duty_End_time', models.TimeField(verbose_name='')),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 183606))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Father_name', models.CharField(max_length=30)),
                ('CNIC', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=2)),
                ('Address', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=30)),
                ('Material_Status', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 182606))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Daily_Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Expenditure_Type', models.CharField(max_length=30)),
                ('Amount', models.CharField(max_length=30)),
                ('Discription', models.CharField(max_length=300)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 197599))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Current_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_Price', models.CharField(max_length=30)),
                ('Number_of_Current_Items', models.CharField(max_length=30)),
                ('SKU', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 198598))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='corderdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=30)),
                ('Price', models.CharField(max_length=30)),
                ('Sales_Price', models.CharField(max_length=30)),
                ('Purchase_Price', models.CharField(max_length=30)),
                ('Discount', models.CharField(max_length=30)),
                ('Corderbooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.corderbooking')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='corderbooking',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
        migrations.CreateModel(
            name='Contact_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LandLine_Number', models.CharField(max_length=30)),
                ('Mobile_Number1', models.CharField(max_length=30)),
                ('Mobile_Number2', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 184606))),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='C_Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Amount', models.CharField(max_length=30)),
                ('Payment_Medium', models.CharField(max_length=30)),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 19, 57, 21, 196598))),
                ('Corderbooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.corderbooking')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
    ]
