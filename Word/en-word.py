import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

data_template_path= r'C:\Users\Panupong Jindarat\Documents\GitHub\automation\Word\en-template-manager-info.docx'

doc = DocxTemplate(data_template_path)
my_name = "Frank Andrade"
my_phone = "(123) 456-789"
my_email = "frank@gmail.com"
my_address = "123 Main Street, NY"
today_date = datetime.today().strftime("%d %b, %Y")

my_context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
              'today_date': today_date}

data_path = r'C:\Users\Panupong Jindarat\Documents\GitHub\automation\Word\en_fake_data.csv'

df = pd.read_csv(data_path)

for index, row in df.iterrows():
    context = {'hiring_manager_name': row['name'],
               'address': row['address'],
               'phone_number': row['phone_number'],
               'email': row['email'],
               'job_position': row['job'],
               'company_name': row['company']}

    context.update(my_context) #เอา dict 'my_context' มาต่อหลัง dict 'context'

    doc.render(context) #เอา context ไปแปะในแต่ละ {{var}} ใน doc 

    exported_data_path = fr'C:\Users\Panupong Jindarat\Documents\GitHub\automation\result\{row['name']}.docx'

    doc.save(exported_data_path)
