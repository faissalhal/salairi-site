"""Générateur du site vitrine salairi.ma (FR / AR / EN).

Usage : python3 tools/build.py   (depuis la racine du dépôt) — régénère les pages HTML, sitemap.xml et robots.txt.
Aucune donnée de grille ni méthode de calcul n'est publiée ici : uniquement la présentation et le barème public de l'IR.
"""
import json, os, datetime, html

SITE = 'https://salairi.ma'
PLAY = 'https://play.google.com/store/apps/details?id=ma.salairi.app'
EMAIL = 'salairi.maroc@gmail.com'
TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ['fr', 'ar', 'en']
PREFIX = {'fr': '', 'ar': '/ar', 'en': '/en'}
DIR = {'fr': 'ltr', 'ar': 'rtl', 'en': 'ltr'}
LOCALE = {'fr': 'fr_MA', 'ar': 'ar_MA', 'en': 'en_US'}
e = html.escape

# ---------------------------------------------------------------- Textes
T = {
'fr': dict(
  nav_sim='Simulateur en ligne', nav_guides='Guides', guides_title='Guides salaire et impôt au Maroc | Salairi', guides_desc='Guides pratiques sur le salaire au Maroc : bulletin de paie du fonctionnaire, salaire net dans le privé, mutuelles et fondations, barème de l’IR 2026-2030.', guides_h1='Guides : salaire, bulletin de paie et impôt au Maroc', guides_intro='Des explications simples, à jour des règles 2026 et de la réforme de l’IR, pour comprendre votre salaire.', read_also='À lire aussi', sim_cta='Simuler en ligne',
  nav_features='Fonctionnalités', nav_reform='Réforme IR 2027', nav_faq='Questions', nav_privacy='Confidentialité', nav_legal='Mentions légales',
  home_title='Salairi — Calcul du salaire net au Maroc 2026-2030 | Fonction publique et privé',
  home_desc='Calculez votre salaire net au Maroc et son évolution de 2026 à 2030 avec la réforme de l’IR : fonction publique (ministère, cadre, grade, échelon) et secteur privé. Application Android gratuite.',
  badge='Réforme de l’IR — loi de finances 2027',
  h1='Calculez votre salaire net au Maroc, de 2026 à 2030',
  lead='Fonctionnaire ou salarié du privé : Salairi vous montre votre salaire net aujourd’hui et ce que la réforme de l’impôt sur le revenu va changer chaque année.',
  cta='Disponible sur Google Play', cta_small='Gratuit · Android · Français, arabe, anglais', soon='Bientôt sur Google Play',
  f_title='Tout votre salaire, clairement',
  features=[
    ('Fonction publique sans saisie de salaire', 'Choisissez votre ministère, votre corps, votre cadre, votre grade et votre échelon : le bulletin se calcule tout seul.'),
    ('Secteur privé en un chiffre', 'Saisissez votre net actuel : Salairi reconstitue le brut, la CNSS, l’AMO et l’IR.'),
    ('Bulletin détaillé par rubrique', 'Émoluments, retraite, AMO, mutuelle (MGEN, MGPAP, OMFAM), œuvres sociales et impôt sur le revenu.'),
    ('Projection 2027-2030', 'Gain mensuel et cumulé, et la part due à la réforme fiscale. Export PDF et simulations enregistrées.'),
  ],
  how_title='Comment ça marche', how=[('Choisissez votre secteur', 'Fonction publique ou secteur privé.'), ('Décrivez votre situation', 'Cadre, grade et échelon, ou votre salaire net ; situation familiale et zone.'), ('Lisez votre bulletin', 'Net par année jusqu’en 2030, rubrique par rubrique.')],
  shots_title='Aperçu de l’application', shots_alt=['Écran d’accueil de Salairi', 'Choix du cadre, du grade et de l’échelon', 'Bulletin de paie simulé', 'Détail des rubriques du bulletin'],
  reform_title='Réforme de l’IR : ce qui change en 2027',
  reform_points=['La tranche exonérée passe de 40 000 DH à 60 000 DH de revenu net imposable par an.', 'Le barème progressif est allégé chaque année jusqu’en 2030 (projet de loi de finances 2027).', 'Les frais professionnels déductibles passent à 45 % (plafond 35 000 DH par an).'],
  reform_more='Voir le barème complet 2026-2030',
  faq_title='Questions fréquentes',
  faq=[
    ('Salairi est-il gratuit ?', 'Oui. L’application est gratuite et financée par la publicité.'),
    ('Mes informations sont-elles envoyées sur internet ?', 'Non. Le calcul se fait sur votre téléphone : votre salaire et votre situation ne quittent jamais l’appareil.'),
    ('Les barèmes 2027 à 2030 sont-ils définitifs ?', 'Non. Ce sont les propositions du projet de loi de finances 2027 ; l’application sera mise à jour après le vote de la loi.'),
    ('Puis-je l’utiliser pour toute la fonction publique ?', 'L’application couvre les principaux corps et grades des ministères (éducation, santé, intérieur, sûreté nationale, justice, finances…). Les grades dont les montants ne sont pas publiés sont signalés.'),
    ('Salairi remplace-t-il mon bulletin de paie ?', 'Non. Les résultats sont des estimations ; seul votre bulletin de paie officiel fait foi.'),
  ],
  disclaimer='Salairi est un outil indépendant, non affilié à l’administration marocaine. Les résultats sont des estimations à titre indicatif.',
  rights='© 2026 Salairi — tous droits réservés.', contact='Contact',
  art_title='Barème de l’IR au Maroc 2026-2030 : la réforme expliquée | Salairi',
  art_desc='Nouveau barème de l’impôt sur le revenu au Maroc : seuil exonéré porté à 60 000 DH en 2027, tranches 2026 à 2030, frais professionnels et exemple chiffré.',
  art_h1='Barème de l’impôt sur le revenu au Maroc : 2026 à 2030',
  art_intro='Le projet de loi de finances 2027 prévoit une réforme progressive de l’impôt sur le revenu (IR) des salariés. Voici les tranches en vigueur en 2026 et celles proposées jusqu’en 2030.',
  art_h2_seuil='Le seuil exonéré passe à 60 000 DH',
  art_seuil='En 2026, le revenu net imposable est exonéré jusqu’à 40 000 DH par an. À partir de 2027, ce seuil passe à 60 000 DH, soit environ 5 000 DH par mois.',
  art_h2_table='Les tranches année par année', art_th=['Année', 'Tranches (revenu net imposable annuel)', 'Statut'],
  art_status_in='En vigueur', art_status_prop='Proposé (PLF 2027)',
  art_h2_other='Frais professionnels et charges de famille',
  art_other=['Frais professionnels : 35 % en 2026 (25 % au-delà de 78 000 DH de brut annuel), 45 % à partir de 2027, plafond 35 000 DH par an.', 'Charges de famille : 600 DH par personne à charge et par an, dans la limite de 6 personnes.'],
  art_h2_ex='Exemple', art_ex='Pour un revenu net imposable de 60 000 DH par an (5 000 DH par mois), sans personne à charge : l’IR est de 2 000 DH par an en 2026 (environ 167 DH par mois) et de 0 DH à partir de 2027.',
  art_note='Les barèmes 2027 à 2030 sont des propositions et peuvent évoluer lors du vote de la loi de finances.',
  art_cta='Calculez votre propre salaire net avec Salairi',
  up_to='jusqu’à', above='au-delà de',
  priv_title='Politique de confidentialité | Salairi', legal_title='Mentions légales et conditions d’utilisation | Salairi',
  nf_title='Page introuvable | Salairi', nf_text='Cette page n’existe pas.', nf_back='Retour à l’accueil',
),
'ar': dict(
  nav_sim='المحاكي على الإنترنت', nav_guides='الدلائل', guides_title='دلائل الأجر والضريبة بالمغرب | Salairi', guides_desc='دلائل عملية حول الأجر بالمغرب: ورقة أداء الموظف، الأجر الصافي في القطاع الخاص، التعاضديات والمؤسسات، جدول الضريبة على الدخل 2026-2030.', guides_h1='دلائل: الأجر وورقة الأداء والضريبة بالمغرب', guides_intro='شروحات مبسطة ومحيّنة وفق قواعد 2026 وإصلاح الضريبة على الدخل، لفهم أجرتك.', read_also='اقرأ أيضاً', sim_cta='احسب على الإنترنت',
  nav_features='المميزات', nav_reform='إصلاح الضريبة 2027', nav_faq='الأسئلة', nav_privacy='الخصوصية', nav_legal='الإشعارات القانونية',
  home_title='Salairi — حساب الأجر الصافي بالمغرب 2026-2030 | الوظيفة العمومية والقطاع الخاص',
  home_desc='احسب أجرتك الصافية بالمغرب وتطورها من 2026 إلى 2030 مع إصلاح الضريبة على الدخل: الوظيفة العمومية (الوزارة، الإطار، الدرجة، الرتبة) والقطاع الخاص. تطبيق أندرويد مجاني.',
  badge='إصلاح الضريبة على الدخل — قانون المالية 2027',
  h1='احسب أجرتك الصافية بالمغرب من 2026 إلى 2030',
  lead='موظفاً كنت أو أجيراً في القطاع الخاص: يُريك Salairi أجرتك الصافية اليوم وما سيغيّره إصلاح الضريبة على الدخل كل سنة.',
  cta='متوفر على Google Play', cta_small='مجاني · أندرويد · العربية والفرنسية والإنجليزية', soon='قريباً على Google Play',
  f_title='أجرتك كاملة، بوضوح',
  features=[
    ('الوظيفة العمومية دون إدخال الأجر', 'اختر وزارتك وهيئتك وإطارك ودرجتك ورتبتك: تُحسب ورقة الأداء تلقائياً.'),
    ('القطاع الخاص برقم واحد', 'أدخل أجرتك الصافية الحالية: يعيد Salairi بناء الأجر الإجمالي والضمان الاجتماعي والتأمين الإجباري والضريبة.'),
    ('ورقة أداء مفصلة حسب البنود', 'المستحقات، التقاعد، التأمين الإجباري، التعاضدية (MGEN وMGPAP وOMFAM)، الأعمال الاجتماعية والضريبة على الدخل.'),
    ('توقعات 2027-2030', 'الربح الشهري والتراكمي والجزء الناتج عن الإصلاح الضريبي. تصدير PDF وحفظ المحاكاة.'),
  ],
  how_title='كيف يعمل', how=[('اختر قطاعك', 'الوظيفة العمومية أو القطاع الخاص.'), ('صف وضعيتك', 'الإطار والدرجة والرتبة، أو أجرتك الصافية؛ الوضعية العائلية والمنطقة.'), ('اقرأ ورقة أدائك', 'الصافي كل سنة حتى 2030، بنداً بنداً.')],
  shots_title='لمحة عن التطبيق', shots_alt=['الشاشة الرئيسية لتطبيق Salairi', 'اختيار الإطار والدرجة والرتبة', 'ورقة الأداء التقديرية', 'تفاصيل بنود ورقة الأداء'],
  reform_title='إصلاح الضريبة على الدخل: ما الذي يتغير في 2027',
  reform_points=['الشريحة المعفاة ترتفع من 40 000 إلى 60 000 درهم من الدخل الصافي الخاضع للضريبة سنوياً.', 'الجدول التصاعدي يُخفف كل سنة حتى 2030 (مشروع قانون المالية 2027).', 'المصاريف المهنية القابلة للخصم ترتفع إلى 45% (بسقف 35 000 درهم سنوياً).'],
  reform_more='الاطلاع على الجدول الكامل 2026-2030',
  faq_title='أسئلة شائعة',
  faq=[
    ('هل Salairi مجاني؟', 'نعم. التطبيق مجاني وممول بالإعلانات.'),
    ('هل تُرسل معطياتي عبر الإنترنت؟', 'لا. يتم الحساب على هاتفك: أجرتك ووضعيتك لا تغادر الجهاز أبداً.'),
    ('هل جداول 2027 إلى 2030 نهائية؟', 'لا. إنها مقترحات مشروع قانون المالية 2027، وسيُحدَّث التطبيق بعد المصادقة على القانون.'),
    ('هل يشمل كل الوظيفة العمومية؟', 'يغطي التطبيق أهم الهيئات والدرجات في الوزارات (التربية، الصحة، الداخلية، الأمن الوطني، العدل، المالية…). والدرجات غير المنشورة مبالغها مُشار إليها.'),
    ('هل يعوض Salairi ورقة الأداء؟', 'لا. النتائج تقديرية، وورقة الأداء الرسمية وحدها هي المرجع.'),
  ],
  disclaimer='Salairi أداة مستقلة غير تابعة للإدارة المغربية. النتائج تقديرية وللاستئناس فقط.',
  rights='© 2026 Salairi — جميع الحقوق محفوظة.', contact='اتصل بنا',
  art_title='جدول الضريبة على الدخل بالمغرب 2026-2030: شرح الإصلاح | Salairi',
  art_desc='الجدول الجديد للضريبة على الدخل بالمغرب: رفع الشريحة المعفاة إلى 60 000 درهم في 2027، الشرائح من 2026 إلى 2030، المصاريف المهنية ومثال بالأرقام.',
  art_h1='جدول الضريبة على الدخل بالمغرب: من 2026 إلى 2030',
  art_intro='ينص مشروع قانون المالية 2027 على إصلاح تدريجي للضريبة على الدخل بالنسبة للأجراء. إليك الشرائح المطبقة في 2026 والمقترحة حتى 2030.',
  art_h2_seuil='الشريحة المعفاة ترتفع إلى 60 000 درهم',
  art_seuil='في 2026، يُعفى الدخل الصافي الخاضع للضريبة حتى 40 000 درهم سنوياً. ابتداءً من 2027، يرتفع هذا السقف إلى 60 000 درهم، أي حوالي 5 000 درهم شهرياً.',
  art_h2_table='الشرائح سنة بسنة', art_th=['السنة', 'الشرائح (الدخل الصافي الخاضع سنوياً)', 'الوضعية'],
  art_status_in='جاري به العمل', art_status_prop='مقترح (مشروع قانون المالية 2027)',
  art_h2_other='المصاريف المهنية والتحملات العائلية',
  art_other=['المصاريف المهنية: 35% في 2026 (25% فوق 78 000 درهم من الأجر الإجمالي السنوي)، و45% ابتداءً من 2027، بسقف 35 000 درهم سنوياً.', 'التحملات العائلية: 600 درهم عن كل شخص في الكفالة سنوياً، في حدود 6 أشخاص.'],
  art_h2_ex='مثال', art_ex='بالنسبة لدخل صافٍ خاضع للضريبة قدره 60 000 درهم سنوياً (5 000 درهم شهرياً)، دون أشخاص في الكفالة: تبلغ الضريبة 2 000 درهم سنوياً في 2026 (حوالي 167 درهماً شهرياً) و0 درهم ابتداءً من 2027.',
  art_note='جداول 2027 إلى 2030 مقترحات وقد تتغير عند التصويت على قانون المالية.',
  art_cta='احسب أجرتك الصافية مع Salairi',
  up_to='حتى', above='أكثر من',
  priv_title='سياسة الخصوصية | Salairi', legal_title='الإشعارات القانونية وشروط الاستعمال | Salairi',
  nf_title='الصفحة غير موجودة | Salairi', nf_text='هذه الصفحة غير موجودة.', nf_back='العودة إلى الرئيسية',
),
'en': dict(
  nav_sim='Online calculator', nav_guides='Guides', guides_title='Salary and tax guides for Morocco | Salairi', guides_desc='Practical guides on salaries in Morocco: the 2026-2030 income tax scale and the 2027 reform. More guides are available in French and Arabic.', guides_h1='Guides: salary and income tax in Morocco', guides_intro='Plain explanations of Moroccan salary rules, up to date with 2026 and the income tax reform. More guides are available in French and Arabic.', read_also='Read also', sim_cta='Calculate online',
  nav_features='Features', nav_reform='2027 tax reform', nav_faq='FAQ', nav_privacy='Privacy', nav_legal='Legal notice',
  home_title='Salairi — Morocco net salary calculator 2026-2030 | Civil service & private sector',
  home_desc='Calculate your net salary in Morocco and how it changes from 2026 to 2030 under the income tax reform: civil service (ministry, position, grade, step) and private sector. Free Android app.',
  badge='Income tax reform — 2027 finance bill',
  h1='Calculate your net salary in Morocco, from 2026 to 2030',
  lead='Civil servant or private-sector employee: Salairi shows your net pay today and what the income tax reform will change each year.',
  cta='Get it on Google Play', cta_small='Free · Android · French, Arabic, English', soon='Coming soon on Google Play',
  f_title='Your whole payslip, clearly',
  features=[
    ('Civil service, no salary to enter', 'Pick your ministry, corps, position, grade and step: the payslip is computed for you.'),
    ('Private sector in one number', 'Enter your current net pay: Salairi rebuilds gross pay, CNSS, AMO and income tax.'),
    ('Payslip broken down by heading', 'Earnings, pension, AMO, mutual insurance (MGEN, MGPAP, OMFAM), welfare foundation and income tax.'),
    ('2027-2030 projection', 'Monthly and cumulative gain, and the share due to the tax reform. PDF export and saved simulations.'),
  ],
  how_title='How it works', how=[('Choose your sector', 'Civil service or private sector.'), ('Describe your situation', 'Position, grade and step, or your net pay; family situation and zone.'), ('Read your payslip', 'Net pay for each year up to 2030, heading by heading.')],
  shots_title='App preview', shots_alt=['Salairi home screen', 'Choosing position, grade and step', 'Simulated payslip', 'Payslip headings in detail'],
  reform_title='Income tax reform: what changes in 2027',
  reform_points=['The tax-free band rises from MAD 40,000 to MAD 60,000 of annual net taxable income.', 'The progressive scale is eased every year until 2030 (2027 draft finance bill).', 'Deductible professional expenses rise to 45% (capped at MAD 35,000 a year).'],
  reform_more='See the full 2026-2030 tax scale',
  faq_title='Frequently asked questions',
  faq=[
    ('Is Salairi free?', 'Yes. The app is free and supported by ads.'),
    ('Is my information sent over the Internet?', 'No. Everything is computed on your phone: your salary and situation never leave the device.'),
    ('Are the 2027-2030 scales final?', 'No. They are the 2027 draft finance bill proposals; the app will be updated once the law is passed.'),
    ('Does it cover the whole civil service?', 'The app covers the main corps and grades of the ministries (education, health, interior, national security, justice, finance…). Grades whose amounts are not published are flagged.'),
    ('Does Salairi replace my payslip?', 'No. Results are estimates; only your official payslip is authoritative.'),
  ],
  disclaimer='Salairi is an independent tool, not affiliated with the Moroccan administration. Results are indicative estimates.',
  rights='© 2026 Salairi — all rights reserved.', contact='Contact',
  art_title='Morocco income tax scale 2026-2030: the reform explained | Salairi',
  art_desc='Morocco’s new income tax scale: tax-free band raised to MAD 60,000 in 2027, brackets from 2026 to 2030, professional expenses and a worked example.',
  art_h1='Morocco income tax scale: 2026 to 2030',
  art_intro='The 2027 draft finance bill plans a gradual reform of employee income tax (IR). Here are the brackets in force in 2026 and those proposed up to 2030.',
  art_h2_seuil='The tax-free band rises to MAD 60,000',
  art_seuil='In 2026, net taxable income is tax-free up to MAD 40,000 a year. From 2027, this threshold rises to MAD 60,000, about MAD 5,000 a month.',
  art_h2_table='Brackets year by year', art_th=['Year', 'Brackets (annual net taxable income)', 'Status'],
  art_status_in='In force', art_status_prop='Proposed (2027 draft bill)',
  art_h2_other='Professional expenses and dependants',
  art_other=['Professional expenses: 35% in 2026 (25% above MAD 78,000 annual gross), 45% from 2027, capped at MAD 35,000 a year.', 'Dependants: MAD 600 per dependant per year, up to 6 people.'],
  art_h2_ex='Example', art_ex='For annual net taxable income of MAD 60,000 (MAD 5,000 a month) with no dependants: income tax is MAD 2,000 a year in 2026 (about MAD 167 a month) and MAD 0 from 2027.',
  art_note='The 2027-2030 scales are proposals and may change when the finance law is voted.',
  art_cta='Calculate your own net salary with Salairi',
  up_to='up to', above='above',
  priv_title='Privacy policy | Salairi', legal_title='Legal notice and terms of use | Salairi',
  nf_title='Page not found | Salairi', nf_text='This page does not exist.', nf_back='Back to home',
),
}
SLUG_ART = {'fr': '/bareme-ir-maroc-2026-2030/', 'ar': '/ar/bareme-ir-maroc-2026-2030/', 'en': '/en/morocco-income-tax-scale-2026-2030/'}

BAREMES = [
    (2026, True, [(40000, 0), (60000, 10), (80000, 20), (100000, 30), (180000, 34), (None, 37)]),
    (2027, False, [(60000, 0), (80000, 10), (100000, 20), (180000, 34), (None, 37)]),
    (2028, False, [(60000, 0), (100000, 10), (200000, 25), (None, 37)]),
    (2029, False, [(60000, 0), (130000, 10), (200000, 20), (None, 35)]),
    (2030, False, [(60000, 0), (150000, 10), (200000, 20), (None, 30)]),
]

def num(n, lang):
    s = f'{n:,}'.replace(',', ' ' if lang != 'en' else ',')
    return s

# ---------------------------------------------------------------- Gabarit
CSS = """
:root{--g:#006233;--g7:#00441F;--g5:#E8F1EC;--gold:#C9A24A;--red:#C1272D;--ink:#14231B;--mut:#4A5A50;--bg:#F6F5F1;--sand:#ECE9E2}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Poppins,"Noto Sans Arabic",system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}
[dir=rtl] body{font-family:"Noto Sans Arabic",Poppins,system-ui,sans-serif}
a{color:var(--g)}img{max-width:100%;height:auto}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.bar{height:4px;background:linear-gradient(90deg,var(--g),var(--gold),var(--red))}
header.top{background:#fff;border-bottom:1px solid var(--sand);position:sticky;top:0;z-index:10}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:10px;padding-bottom:10px}
.top nav{display:flex;align-items:center;gap:18px;font-size:14px}.top nav a{color:var(--ink);text-decoration:none}.top nav a:hover{color:var(--g)}
.langs{display:flex;gap:2px;background:var(--bg);border:1px solid var(--sand);border-radius:10px;padding:2px}.langs a{padding:3px 9px;border-radius:7px;font-size:13px;font-weight:600;color:var(--mut);text-decoration:none}.langs a.on{background:var(--g);color:#fff}
.hero{background:var(--g);color:#fff;position:relative;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center;padding-top:56px;padding-bottom:56px}
.pill{display:inline-block;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);border-radius:99px;padding:5px 14px;font-size:13px}
.hero h1{font-size:clamp(30px,4.4vw,48px);line-height:1.15;margin:18px 0 14px}.hero p.lead{font-size:18px;color:rgba(255,255,255,.88);margin:0 0 26px;max-width:560px}
.btn{display:inline-flex;align-items:center;gap:10px;background:#111;color:#fff;text-decoration:none;border-radius:12px;padding:12px 20px;font-weight:600}
.btn svg{width:22px;height:22px}.btn:hover{background:#000}.small{font-size:13px;color:rgba(255,255,255,.75);margin-top:10px}
.phone{justify-self:center;width:min(300px,80%);border-radius:30px;border:8px solid #0b1a12;box-shadow:0 30px 60px rgba(0,0,0,.35);background:#fff}
section{padding:64px 0}h2{font-size:clamp(24px,3vw,32px);margin:0 0 28px;line-height:1.25}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.card{background:#fff;border-radius:18px;padding:22px;box-shadow:0 1px 2px rgba(20,35,27,.05),0 6px 20px rgba(20,35,27,.06)}
.card h3{font-size:17px;margin:12px 0 6px}.card p{margin:0;color:var(--mut);font-size:15px}.ico{width:42px;height:42px;border-radius:12px;background:var(--g5);display:flex;align-items:center;justify-content:center;color:var(--g);font-weight:700}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;counter-reset:s}.step{background:#fff;border-radius:18px;padding:22px;border-top:4px solid var(--gold)}.step b{display:block;font-size:17px;margin-bottom:4px}.step p{margin:0;color:var(--mut)}
.shots{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.shots img{border-radius:18px;border:1px solid var(--sand);background:#fff}
.reform{background:#fff}.reform ul{padding-inline-start:20px;font-size:17px}.reform li{margin:8px 0}
.more{display:inline-block;margin-top:10px;font-weight:600}
details{background:#fff;border-radius:14px;padding:16px 20px;margin:10px 0;border:1px solid var(--sand)}summary{cursor:pointer;font-weight:600}details p{margin:10px 0 0;color:var(--mut)}
.cta{background:var(--g7);color:#fff;text-align:center;border-radius:24px;padding:40px 20px}.cta h2{margin-bottom:18px}
footer{background:var(--g);color:rgba(255,255,255,.82);font-size:14px;padding:36px 0}footer a{color:#fff}footer .row{display:flex;flex-wrap:wrap;gap:18px;margin:14px 0}
article{background:#fff;border-radius:22px;padding:36px;margin:36px auto;max-width:860px}article h1{font-size:clamp(26px,3.6vw,38px);line-height:1.2;margin-top:0}article h2{font-size:22px;margin:30px 0 12px}
table{width:100%;border-collapse:collapse;font-size:15px}th,td{border-bottom:1px solid var(--sand);padding:10px 8px;text-align:start;vertical-align:top}th{background:var(--g5)}
.tag{display:inline-block;font-size:12px;border-radius:99px;padding:2px 10px;background:#FFF4D6;color:#7a5a00}.tag.in{background:var(--g5);color:var(--g7)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}.grid2 .card{box-shadow:none;border:1px solid var(--sand)}.grid2 h3{margin-top:0}.muted{color:var(--mut);font-size:14px}.note{background:var(--bg);border-radius:12px;padding:12px 16px;color:var(--mut);font-size:14px}
@media (max-width:900px){.hero .wrap{grid-template-columns:1fr}.grid4{grid-template-columns:1fr 1fr}.shots{grid-template-columns:1fr 1fr}.steps{grid-template-columns:1fr}.top nav .hide{display:none}}
@media (max-width:560px){.grid4,.grid2{grid-template-columns:1fr}article{padding:22px}}
"""

PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#34A853" d="M3.6 1.8 13.4 12l-9.8 10.2c-.4-.2-.6-.6-.6-1.1V2.9c0-.5.2-.9.6-1.1z"/><path fill="#FBBC04" d="m16.8 8.6-3.4 3.4 3.4 3.4 3.9-2.2c.8-.5.8-1.7 0-2.2z"/><path fill="#4285F4" d="M3.6 22.2 13.4 12l3.4 3.4-11.5 6.6c-.6.3-1.2.4-1.7.2z"/><path fill="#EA4335" d="M3.6 1.8c.5-.2 1.1-.1 1.7.2l11.5 6.6-3.4 3.4z"/></svg>'

def alternates(paths):
    out = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{paths[l]}">' for l in LANGS if l in paths)
    return out + f'<link rel="alternate" hreflang="x-default" href="{SITE}{paths["fr"]}">'

def page(lang, path, title, desc, body, paths, jsonld=None, og_type='website'):
    t = T[lang]
    langs = ''.join(f'<a href="{paths.get(l, PREFIX[l] + '/')}" hreflang="{l}" class="{"on" if l == lang else ""}" lang="{l}">{ {"fr": "FR", "ar": "ع", "en": "EN"}[l] }</a>' for l in LANGS)
    home = PREFIX[lang] + '/'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{DIR[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{path}">
{alternates(paths)}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Salairi"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}/img/og.jpg"><meta property="og:locale" content="{LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#006233">
<meta name="google-adsense-account" content="ca-pub-9525234825796734">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9525234825796734" crossorigin="anonymous"></script>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Noto+Sans+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
{ld}
</head>
<body>
<div class="bar"></div>
<header class="top"><div class="wrap">
<a href="{home}" aria-label="Salairi"><img src="/img/logo.svg" alt="Salairi" width="170" height="50"></a>
<nav><a href="/simulateur/?lang={lang}" style="font-weight:600;color:var(--g)">{t['nav_sim']}</a><a class="hide" href="{home}#fonctionnalites">{t['nav_features']}</a><a class="hide" href="{SLUG_GUIDES[lang]}">{t['nav_guides']}</a><a class="hide" href="{SLUG_ART[lang]}">{t['nav_reform']}</a><a class="hide" href="{home}#faq">{t['nav_faq']}</a><div class="langs">{langs}</div></nav>
</div></header>
<main>{body}</main>
<footer><div class="wrap">
<img src="/img/logo-white.svg" alt="Salairi" width="150" height="44" loading="lazy">
<div class="row"><a href="/simulateur/?lang={lang}">{t['nav_sim']}</a><a href="{SLUG_GUIDES[lang]}">{t['nav_guides']}</a><a href="{SLUG_ART[lang]}">{t['nav_reform']}</a><a href="/confidentialite/">{t['nav_privacy']}</a><a href="/mentions-legales/">{t['nav_legal']}</a><a href="mailto:{EMAIL}">{t['contact']}</a></div>
<p>{t['disclaimer']}</p><p>{t['rights']}</p>
</div></footer>
</body></html>'''

def play_button(lang):
    t = T[lang]
    return (f'<div style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn" href="{PLAY}" rel="noopener">{PLAY_SVG}<span>{t["cta"]}</span></a>'
            f'<a class="btn" style="background:#fff;color:var(--g)" href="/simulateur/?lang={lang}">{t["sim_cta"]} →</a></div><p class="small">{t["cta_small"]}</p>')

def home(lang):
    t = T[lang]
    paths = {l: PREFIX[l] + '/' for l in LANGS}
    feats = ''.join(f'<div class="card"><div class="ico">{i+1}</div><h3>{e(a)}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(t['features']))
    steps = ''.join(f'<div class="step"><b>{e(a)}</b><p>{e(b)}</p></div>' for a, b in t['how'])
    names = ['1-accueil', '2-formulaire', '3-bulletin', '4-rubriques']
    shots = ''.join(f'<img src="/img/{lang}-{n}.webp" alt="{e(t["shots_alt"][i])}" width="540" height="960" loading="lazy">' for i, n in enumerate(names))
    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in t['faq'])
    reform = ''.join(f'<li>{e(p)}</li>' for p in t['reform_points'])
    body = f'''
<section class="hero"><div class="wrap">
<div><span class="pill">{t['badge']}</span><h1>{e(t['h1'])}</h1><p class="lead">{e(t['lead'])}</p>{play_button(lang)}</div>
<img class="phone" src="/img/{lang}-3-bulletin.webp" alt="{e(t['shots_alt'][2])}" width="540" height="960" fetchpriority="high">
</div></section>
<section id="fonctionnalites"><div class="wrap"><h2>{t['f_title']}</h2><div class="grid4">{feats}</div></div></section>
<section style="padding-top:0"><div class="wrap"><h2>{t['how_title']}</h2><div class="steps">{steps}</div></div></section>
<section class="reform" id="reforme"><div class="wrap"><h2>{t['reform_title']}</h2><ul>{reform}</ul><a class="more" href="{SLUG_ART[lang]}">{t['reform_more']} →</a></div></section>
<section><div class="wrap"><h2>{t['shots_title']}</h2><div class="shots">{shots}</div></div></section>
<section id="faq" style="padding-top:0"><div class="wrap"><h2>{t['faq_title']}</h2>{faq}</div></section>
<section style="padding-top:0"><div class="wrap"><div class="cta"><h2>{e(t['h1'])}</h2>{play_button(lang)}</div></div></section>'''
    ld = [
        {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'Salairi', 'operatingSystem': 'Android',
         'applicationCategory': 'FinanceApplication', 'inLanguage': ['fr', 'ar', 'en'], 'description': t['home_desc'], 'url': SITE + paths[lang],
         'downloadUrl': PLAY, 'image': SITE + '/img/og.jpg', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'MAD'}},
        {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in t['faq']]},
        {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Salairi', 'url': SITE, 'logo': SITE + '/img/icon-192.png', 'email': EMAIL},
    ]
    return paths[lang], page(lang, paths[lang], t['home_title'], t['home_desc'], body, paths, ld)

def article(lang):
    t = T[lang]
    rows = ''
    for year, inforce, br in BAREMES:
        lo = 0; parts = []
        for up, rate in br:
            if up is None: parts.append(f'{t["above"]} {num(lo, lang)} : {rate} %' if lang == 'fr' else f'{t["above"]} {num(lo, lang)}: {rate}%')
            else: parts.append(f'{num(lo, lang)} – {num(up, lang)} : {rate} %' if lang == 'fr' else f'{num(lo, lang)} – {num(up, lang)}: {rate}%')
            lo = up
        tag = f'<span class="tag in">{t["art_status_in"]}</span>' if inforce else f'<span class="tag">{t["art_status_prop"]}</span>'
        rows += f'<tr><td><b>{year}</b></td><td>{"<br>".join(parts)}</td><td>{tag}</td></tr>'
    other = ''.join(f'<li>{e(x)}</li>' for x in t['art_other'])
    body = f'''<article>
<h1>{e(t['art_h1'])}</h1>
<p>{e(t['art_intro'])}</p>
<h2>{e(t['art_h2_seuil'])}</h2><p>{e(t['art_seuil'])}</p>
<h2>{e(t['art_h2_table'])}</h2>
<table><thead><tr>{''.join(f'<th>{e(h)}</th>' for h in t['art_th'])}</tr></thead><tbody>{rows}</tbody></table>
<h2>{e(t['art_h2_other'])}</h2><ul>{other}</ul>
<h2>{e(t['art_h2_ex'])}</h2><p>{e(t['art_ex'])}</p>
<p class="note">{e(t['art_note'])}</p>
<div class="cta" style="margin-top:28px"><h2>{e(t['art_cta'])}</h2>{play_button(lang)}</div>
</article>'''
    ld = [{'@context': 'https://schema.org', '@type': 'Article', 'headline': t['art_h1'], 'description': t['art_desc'], 'inLanguage': lang,
           'datePublished': '2026-11-02', 'dateModified': TODAY, 'author': {'@type': 'Organization', 'name': 'Salairi'},
           'publisher': {'@type': 'Organization', 'name': 'Salairi', 'logo': {'@type': 'ImageObject', 'url': SITE + '/img/icon-192.png'}},
           'image': SITE + '/img/og.jpg', 'mainEntityOfPage': SITE + SLUG_ART[lang]}]
    return SLUG_ART[lang], page(lang, SLUG_ART[lang], t['art_title'], t['art_desc'], body, SLUG_ART, ld, 'article')

from articles import ARTICLES
SLUG_GUIDES = {'fr': '/guides/', 'ar': '/ar/guides/', 'en': '/en/guides/'}

def guide_list(lang, exclude=None):
    items = [(a['slug'][lang], a['h1'][lang], a['desc'][lang]) for a in ARTICLES if lang in a['slug'] and a['id'] != exclude]
    if exclude != 'ir': items.append((SLUG_ART[lang], T[lang]['art_h1'], T[lang]['art_desc']))
    return ''.join(f'<div class="card"><h3><a href="{u}">{e(h)}</a></h3><p>{e(d)}</p></div>' for u, h, d in items)

def article_ld(lang, h1, desc, url, date):
    return [{'@context': 'https://schema.org', '@type': 'Article', 'headline': h1, 'description': desc, 'inLanguage': lang,
             'datePublished': date, 'dateModified': TODAY, 'author': {'@type': 'Organization', 'name': 'Salairi'},
             'publisher': {'@type': 'Organization', 'name': 'Salairi', 'logo': {'@type': 'ImageObject', 'url': SITE + '/img/icon-192.png'}},
             'image': SITE + '/img/og.jpg', 'mainEntityOfPage': SITE + url}]

def guide_article(a, lang):
    t = T[lang]; url = a['slug'][lang]
    body = f'''<article>
<h1>{e(a['h1'][lang])}</h1>
{a['body'][lang]}
<div class="cta" style="margin-top:28px"><h2>{e(t['art_cta'])}</h2>{play_button(lang)}</div>
<h2>{t['read_also']}</h2><div class="grid2">{guide_list(lang, a['id'])}</div>
</article>'''
    return url, page(lang, url, a['title'][lang], a['desc'][lang], body, a['slug'], article_ld(lang, a['h1'][lang], a['desc'][lang], url, a['date']), 'article')

def guides_index(lang):
    t = T[lang]; url = SLUG_GUIDES[lang]
    body = f'<article><h1>{e(t["guides_h1"])}</h1><p>{e(t["guides_intro"])}</p><div class="grid2">{guide_list(lang)}</div><div class="cta" style="margin-top:28px"><h2>{e(t["art_cta"])}</h2>{play_button(lang)}</div></article>'
    return url, page(lang, url, t['guides_title'], t['guides_desc'], body, SLUG_GUIDES)

def static_page(lang, slug, title, inner_file):
    paths = {l: f'/{slug}/' for l in LANGS}
    inner = open(os.path.join(ROOT, 'tools', inner_file), encoding='utf-8').read()
    body = f'<article>{inner}</article>'
    return paths[lang], page(lang, paths[lang], T[lang][title], T[lang][title].split(' | ')[0], body, paths)

def write(path, content):
    p = os.path.join(ROOT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(ROOT, path.strip('/'))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(content)

urls = []
for lang in LANGS:
    for fn in (home, article, guides_index):
        path, content = fn(lang); write(path, content); urls.append(path)
    for a in ARTICLES:
        if lang in a['slug']:
            path, content = guide_article(a, lang); write(path, content); urls.append(path)
for slug, title, f in [('confidentialite', 'priv_title', 'privacy.html'), ('mentions-legales', 'legal_title', 'legal.html')]:
    path, content = static_page('fr', slug, title, f); write(path, content); urls.append(path)  # pages trilingues : une seule adresse

# 404, redirection de l'ancienne adresse de confidentialité
t = T['fr']
open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8').write(page('fr', '/404.html', t['nf_title'], t['nf_text'], f'<article><h1>{t["nf_title"].split(" | ")[0]}</h1><p>{t["nf_text"]}</p><p><a href="/">{t["nf_back"]}</a></p></article>', {l: PREFIX[l] + '/' for l in LANGS}).replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"'))
open(os.path.join(ROOT, 'privacy.html'), 'w', encoding='utf-8').write('<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/confidentialite/"><link rel="canonical" href="https://salairi.ma/confidentialite/"><a href="/confidentialite/">Politique de confidentialité</a>')

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
groups = [{l: PREFIX[l] + '/' for l in LANGS}, SLUG_ART, SLUG_GUIDES] + [a['slug'] for a in ARTICLES]
for s_ in ('confidentialite', 'mentions-legales'):
    sitemap.append(f'<url><loc>{SITE}/{s_}/</loc><lastmod>{TODAY}</lastmod></url>')
sitemap.append(f'<url><loc>{SITE}/simulateur/</loc><lastmod>{TODAY}</lastmod></url>')
for g in groups:
    for l in [x for x in LANGS if x in g]:
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{k}" href="{SITE}{g[k]}"/>' for k in LANGS if k in g)
        sitemap.append(f'<url><loc>{SITE}{g[l]}</loc><lastmod>{TODAY}</lastmod>{alts}</url>')
sitemap.append('</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sitemap))
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n')
print(len(urls), 'pages générées')
