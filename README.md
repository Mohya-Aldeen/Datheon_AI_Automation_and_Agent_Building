Datheon: AI Automation & Agent Building

Internship project repository for the Datheon AI Automation & Agent Building program.

Author: Mohya-Aldeen Kudaish | GitHub: @Mohya-Aldeen | LinkedIn: Mohya-Aldeen

English · العربية

English
Purpose

This repository holds three working AI automations built with Make.com and the OpenAI API. Each one replaces a slow, manual business process with a workflow that runs on its own:

Sales leads are captured, scored by AI, stored, and sent to the sales team in seconds.
Customer emails are read, classified, labelled, and answered with a draft reply for human review.
Paper receipts are read by AI vision and written into an accounting spreadsheet automatically.
Task status

The program requires completing two or three tasks. All three are done.

Task	Title	Status
1	Multi-Source Lead Routing & Instant AI Qualification	Complete: see task-1-lead-routing
2	Autonomous Customer Support & Intelligent Email Triage	Complete: see Task2_AI_Email_Triage
3	AI Vision Invoice Scanner & Accounting Sync	Complete: see Task-(3)-ai-invoice-scanner-make
Task 1 at a glance: Lead routing
A lead arrives from two sources: a Python script that posts JSON to a webhook, and a Tally web form.
The Tally response is converted by a small second scenario (Scenario B) into the same flat format and forwarded to the same webhook, so every source follows one path.
OpenAI reads the lead and returns strict JSON: a Hot / Warm / Cold label, a 0 to 100 score, estimated company size and budget, a one-sentence reason, and three talking points.
Airtable stores one record per lead.
Slack posts an alert with the verdict, the reason, and the talking points.
Task 2 at a glance: Email triage
On a schedule, the workflow reads new customer emails in Gmail.
OpenAI classifies each email by category, sentiment, and urgency, and the workflow applies Gmail labels such as Urgent and Billing.
Approved answers are retrieved from a Google Sheets knowledge base.
A reply is drafted for human review, with guardrails against invented promises and prompt injection.
Task 3 at a glance: Invoice scanner
A PDF receipt is dropped into a Google Drive folder ("Invoices - Inbox").
Make.com watches the folder, notices the new file, and downloads it.
OpenAI Vision reads the receipt and extracts the vendor, invoice date, line items, and tax amounts.
The extracted data is inserted into Google Sheets, so no one has to type expenses by hand.
A live scheduled run was tested end to end. Screenshots are in the task folder.
Tools used
Tool	Role
Make.com	Orchestration: webhooks, scheduling, scenario logic, connectors
OpenAI API	Lead qualification, email classification, reply drafting
OpenAI Vision	Reading PDF receipts and extracting structured data
Airtable	Database of qualified leads
Slack	Real-time alerts to the sales team
Tally	Public lead form (second lead source)
Gmail	Source of customer emails, labels, and drafts
Google Sheets	Email knowledge base and expense records
Google Drive	Inbox folder for receipts
Python (requests)	Test client: sample and edge-case leads
GitHub	Version control and submission
Key results
Task 1: end-to-end time of about 4 seconds (main scenario 3 s, Scenario B under 1 s), measured in Make's run history. The requirement was under 10 seconds. Tested with edge cases: empty fields, vague budget wording, and text with quotation marks and symbols.
Task 2: emails are classified and labelled automatically, and replies are drafted from approved answers only, then left for a human to review.
Task 3: receipts dropped into the folder are read and logged to the spreadsheet without manual typing.
Repository structure
Datheon_AI_Automation_and_Agent_Building/
├── README.md
├── .gitignore
├── .env.example
├── task-1-lead-routing/
├── Task2_AI_Email_Triage/
└── Task-(3)-ai-invoice-scanner-make/

Each task folder has its own README with architecture, setup, results, and lessons learned.

Security

No secrets are stored in this repo. The webhook URL is read from an environment variable or a local .env file (ignored by Git), and API keys live only inside Make's connections.

العربية
الهدف

يضم هذا المستودع ثلاث أنظمة أتمتة تعمل بالذكاء الاصطناعي، مبنية باستخدام Make.com وواجهة OpenAI. كل نظام يستبدل عملية يدوية بطيئة بسير عمل يعمل تلقائيًا:

العملاء المحتملون يُلتقطون ويُقيَّمون بالذكاء الاصطناعي ويُحفظون ويصلون لفريق المبيعات خلال ثوانٍ.
رسائل العملاء تُقرأ وتُصنَّف وتُوسَم، ثم تُجهَّز لها مسودة رد لمراجعة بشرية.
الفواتير الورقية يقرؤها الذكاء الاصطناعي بالرؤية الحاسوبية وتُسجَّل تلقائيًا في جدول المحاسبة.
حالة المهام

يشترط البرنامج إنجاز مهمتين أو ثلاث. وقد اكتملت المهام الثلاث.

المهمة	العنوان	الحالة
1	توجيه العملاء المحتملين من مصادر متعددة وتقييمهم فورًا بالذكاء الاصطناعي	مكتملة: انظر task-1-lead-routing
2	دعم العملاء الآلي وفرز البريد الإلكتروني الذكي	مكتملة: انظر Task2_AI_Email_Triage
3	قارئ الفواتير بالرؤية الحاسوبية ومزامنة المحاسبة	مكتملة: انظر Task-(3)-ai-invoice-scanner-make
المهمة الأولى باختصار: توجيه العملاء المحتملين
يصل العميل المحتمل من مصدرين: سكربت بايثون يرسل بيانات JSON إلى Webhook، ونموذج ويب من Tally.
يحوّل سيناريو ثانٍ (Scenario B) بيانات Tally إلى الصيغة الموحدة نفسها ويرسلها إلى Webhook ذاته، فيسلك كل مصدر المسار نفسه.
يقرأ OpenAI بيانات العميل ويعيد نتيجة بصيغة JSON صارمة: التصنيف Hot / Warm / Cold، ودرجة من 0 إلى 100، وحجم الشركة والميزانية المقدّرين، وسببًا في جملة واحدة، وثلاث نقاط حوار.
يحفظ Airtable سجلًا واحدًا لكل عميل.
يرسل Slack تنبيهًا يتضمن التصنيف والسبب ونقاط الحوار.
المهمة الثانية باختصار: فرز البريد الإلكتروني
يقرأ سير العمل رسائل العملاء الجديدة في Gmail وفق جدول زمني.
يصنّف OpenAI كل رسالة حسب الفئة والمشاعر ودرجة الاستعجال، ثم تُضاف وسوم Gmail مثل Urgent وBilling.
تُجلب الإجابات المعتمدة من قاعدة معرفة في Google Sheets.
تُجهَّز مسودة رد لمراجعة بشرية، مع ضوابط تمنع الوعود المختلقة وهجمات حقن التعليمات.
المهمة الثالثة باختصار: قارئ الفواتير
يُوضع ملف PDF للفاتورة في مجلد على Google Drive (باسم "Invoices - Inbox").
يراقب Make.com المجلد، ويكتشف الملف الجديد ويحمّله.
يقرأ OpenAI Vision الفاتورة ويستخرج اسم المورّد وتاريخ الفاتورة وبنودها ومبالغ الضريبة.
تُدرَج البيانات المستخرجة في Google Sheets، فلا يحتاج أحد إلى إدخال المصروفات يدويًا.
جرى اختبار تشغيل مجدول حقيقي من البداية إلى النهاية، ولقطات الشاشة في مجلد المهمة.
الأدوات المستخدمة
الأداة	دورها
Make.com	تنسيق سير العمل: Webhooks والجدولة والمنطق والموصّلات
OpenAI API	تقييم العملاء، وتصنيف الرسائل، وصياغة الردود
OpenAI Vision	قراءة الفواتير بصيغة PDF واستخراج بيانات منظمة
Airtable	قاعدة بيانات العملاء المقيَّمين
Slack	تنبيهات فورية لفريق المبيعات
Tally	نموذج التقاط العملاء (المصدر الثاني)
Gmail	مصدر رسائل العملاء والوسوم والمسودات
Google Sheets	قاعدة المعرفة وسجلات المصروفات
Google Drive	مجلد استقبال الفواتير
Python (requests)	عميل اختبار: عملاء تجريبيون وحالات صعبة
GitHub	إدارة الإصدارات والتسليم
أهم النتائج
المهمة 1: زمن التنفيذ الكامل نحو 4 ثوانٍ (السيناريو الرئيسي 3 ثوانٍ، وسيناريو Tally أقل من ثانية)، حسب سجل التشغيل في Make. والمطلوب أقل من 10 ثوانٍ. واختُبرت حالات صعبة: حقول فارغة، وميزانية غير واضحة، ونص يحتوي علامات اقتباس ورموزًا.
المهمة 2: تُصنَّف الرسائل وتُوسَم تلقائيًا، وتُجهَّز الردود من إجابات معتمدة فقط ثم تُترك لمراجعة بشرية.
المهمة 3: الفواتير التي تُوضع في المجلد تُقرأ وتُسجَّل في الجدول دون إدخال يدوي.
هيكل المستودع
Datheon_AI_Automation_and_Agent_Building/
├── README.md
├── .gitignore
├── .env.example
├── task-1-lead-routing/
├── Task2_AI_Email_Triage/
└── Task-(3)-ai-invoice-scanner-make/

لكل مهمة ملف README خاص بها يشرح البنية والإعداد والنتائج والدروس المستفادة.
