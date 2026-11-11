"""Guides supplémentaires (novembre 2026) — FR / AR. Règles publiques uniquement."""

SRC_FR = '<p class="note">Sources officielles : <a href="https://www.tax.gov.ma" rel="noopener" target="_blank">Direction générale des impôts</a> · <a href="https://www.sgg.gov.ma" rel="noopener" target="_blank">Bulletin officiel (SGG)</a> · <a href="https://www.cnss.ma" rel="noopener" target="_blank">CNSS</a>. Salairi est un site indépendant, non affilié au gouvernement.</p>'
SRC_AR = '<p class="note">المصادر الرسمية: <a href="https://www.tax.gov.ma" rel="noopener" target="_blank">المديرية العامة للضرائب</a> · <a href="https://www.sgg.gov.ma" rel="noopener" target="_blank">الجريدة الرسمية (الأمانة العامة للحكومة)</a> · <a href="https://www.cnss.ma" rel="noopener" target="_blank">الصندوق الوطني للضمان الاجتماعي</a>. Salairi موقع مستقل غير تابع للحكومة.</p>'

ARTICLES2 = [
{
 'id': 'calcul-ir', 'date': '2026-11-11',
 'slug': {'fr': '/calcul-ir-salaire-maroc/', 'ar': '/ar/calcul-ir-salaire-maroc/'},
 'title': {'fr': 'Calcul de l’IR sur salaire au Maroc : méthode pas à pas avec exemple (2026) | Salairi',
           'ar': 'حساب الضريبة على الدخل من الأجر بالمغرب: الطريقة خطوة بخطوة مع مثال (2026) | Salairi'},
 'desc': {'fr': 'Comment calculer soi-même l’impôt sur le revenu retenu sur un salaire au Maroc : frais professionnels, cotisations, barème mensuel, charges de famille. Exemple complet pour un brut de 11 444 DH.',
          'ar': 'كيف تحسب بنفسك الضريبة على الدخل المقتطعة من الأجر بالمغرب: المصاريف المهنية، الاشتراكات، الجدول الشهري، التحملات العائلية. مثال كامل لأجر إجمالي قدره 11 444 درهماً.'},
 'h1': {'fr': 'Calculer l’IR sur son salaire : la méthode pas à pas', 'ar': 'حساب الضريبة على الدخل من الأجر: الطريقة خطوة بخطوة'},
 'body': {
'fr': '''
<p>L’impôt sur le revenu (IR) est retenu chaque mois par l’employeur. Le calcul suit toujours les mêmes cinq étapes. Nous les appliquons ici à un salarié du privé, célibataire, dont le salaire brut est de <b>11 444,14 DH par mois</b> en 2026.</p>
<h2>Étape 1 : le salaire brut imposable</h2>
<p>On part du salaire brut, primes et avantages compris, mais <b>sans</b> les indemnités exonérées (transport, panier, représentation… dans les limites fixées par l’administration fiscale). Ici : 11 444,14 DH.</p>
<h2>Étape 2 : les frais professionnels</h2>
<p>Une déduction forfaitaire couvre les frais liés au travail. En 2026, elle est de <b>35 %</b> si le brut annuel ne dépasse pas 78 000 DH, et de <b>25 %</b> au-delà, avec un plafond de 35 000 DH par an. Notre salarié gagne 137 330 DH par an : on applique 25 %, soit <b>2 861,04 DH</b> par mois.</p>
<h2>Étape 3 : les cotisations déductibles</h2>
<ul><li>CNSS : 4,48 % plafonnés à 6 000 DH, soit <b>268,80 DH</b> ;</li><li>AMO : 2,26 % du brut, soit <b>258,64 DH</b> ;</li><li>s’il y en a : CIMR, mutuelle, intérêts d’un prêt logement principal.</li></ul>
<h2>Étape 4 : le revenu net imposable</h2>
<p>11 444,14 − 2 861,04 − 268,80 − 258,64 = <b>8 055,66 DH</b>.</p>
<h2>Étape 5 : le barème et les charges de famille</h2>
<p>On applique le barème mensuel avec sa « somme à déduire » :</p>
<table><thead><tr><th>Net imposable mensuel</th><th>Taux</th><th>Somme à déduire</th></tr></thead><tbody>
<tr><td>jusqu’à 3 333,33 DH</td><td>0 %</td><td>0</td></tr>
<tr><td>3 333,34 à 5 000 DH</td><td>10 %</td><td>333,33</td></tr>
<tr><td>5 000,01 à 6 666,67 DH</td><td>20 %</td><td>833,33</td></tr>
<tr><td>6 666,68 à 8 333,33 DH</td><td>30 %</td><td>1 500,00</td></tr>
<tr><td>8 333,34 à 15 000 DH</td><td>34 %</td><td>1 833,33</td></tr>
<tr><td>au-delà de 15 000 DH</td><td>37 %</td><td>2 283,33</td></tr>
</tbody></table>
<p>8 055,66 × 30 % − 1 500 = <b>916,70 DH</b> d’IR par mois. Pour un salarié marié avec deux enfants, on retire 50 DH par personne à charge (600 DH par an), soit 150 DH : l’IR tomberait à 766,70 DH.</p>
<h2>Résultat</h2>
<p>Salaire net = 11 444,14 − 268,80 − 258,64 − 916,70 = <b>10 000 DH</b>.</p>
<h2>Ce qui change avec la réforme</h2>
<p>Le projet de loi de finances 2027 propose de relever les frais professionnels et d’alléger le barème jusqu’en 2030. Avec les mêmes 11 444 DH bruts, le net passerait à environ 10 483 DH en 2027 et 10 617 DH en 2030. Détails dans notre article sur le <a href="/bareme-ir-maroc-2026-2030/">barème de l’IR 2026-2030</a>, et calcul personnalisé avec le <a href="/simulateur/?lang=fr">simulateur</a>.</p>
''' + SRC_FR,
'ar': '''
<p>تقتطع المقاولة الضريبة على الدخل كل شهر. ويتبع الحساب دائماً خمس خطوات، نطبقها هنا على أجير في القطاع الخاص، أعزب، أجره الإجمالي <b>11 444,14 درهماً شهرياً</b> في 2026.</p>
<h2>الخطوة 1: الأجر الإجمالي الخاضع للضريبة</h2>
<p>ننطلق من الأجر الإجمالي بما فيه المنح والامتيازات، <b>دون</b> التعويضات المعفاة (النقل، السلة، التمثيل… في الحدود التي تحددها الإدارة الجبائية). هنا: 11 444,14 درهماً.</p>
<h2>الخطوة 2: المصاريف المهنية</h2>
<p>خصم جزافي يغطي مصاريف العمل. في 2026 يبلغ <b>35%</b> إذا لم يتجاوز الأجر الإجمالي السنوي 78 000 درهم، و<b>25%</b> فوق ذلك، بسقف 35 000 درهم سنوياً. أجيرنا يتقاضى 137 330 درهماً سنوياً، فنطبق 25%، أي <b>2 861,04 درهماً</b> شهرياً.</p>
<h2>الخطوة 3: الاشتراكات القابلة للخصم</h2>
<ul><li>الضمان الاجتماعي: 4,48% في حدود 6 000 درهم، أي <b>268,80 درهماً</b>؛</li><li>التأمين الإجباري عن المرض: 2,26% من الأجر الإجمالي، أي <b>258,64 درهماً</b>؛</li><li>إن وُجدت: CIMR، التعاضدية، فوائد قرض السكن الرئيسي.</li></ul>
<h2>الخطوة 4: الدخل الصافي الخاضع للضريبة</h2>
<p>11 444,14 − 2 861,04 − 268,80 − 258,64 = <b>8 055,66 درهماً</b>.</p>
<h2>الخطوة 5: الجدول والتحملات العائلية</h2>
<p>نطبق الجدول الشهري مع «المبلغ الواجب خصمه»:</p>
<table><thead><tr><th>الدخل الصافي الشهري</th><th>السعر</th><th>المبلغ الواجب خصمه</th></tr></thead><tbody>
<tr><td>إلى 3 333,33 درهماً</td><td>0%</td><td>0</td></tr>
<tr><td>من 3 333,34 إلى 5 000</td><td>10%</td><td>333,33</td></tr>
<tr><td>من 5 000,01 إلى 6 666,67</td><td>20%</td><td>833,33</td></tr>
<tr><td>من 6 666,68 إلى 8 333,33</td><td>30%</td><td>1 500,00</td></tr>
<tr><td>من 8 333,34 إلى 15 000</td><td>34%</td><td>1 833,33</td></tr>
<tr><td>أكثر من 15 000</td><td>37%</td><td>2 283,33</td></tr>
</tbody></table>
<p>8 055,66 × 30% − 1 500 = <b>916,70 درهماً</b> ضريبة شهرية. بالنسبة لأجير متزوج وله طفلان، نخصم 50 درهماً عن كل شخص في الكفالة (600 درهم سنوياً)، أي 150 درهماً، فتصبح الضريبة 766,70 درهماً.</p>
<h2>النتيجة</h2>
<p>الأجر الصافي = 11 444,14 − 268,80 − 258,64 − 916,70 = <b>10 000 درهم</b>.</p>
<h2>ما الذي يغيّره الإصلاح</h2>
<p>يقترح مشروع قانون المالية 2027 رفع المصاريف المهنية وتخفيف الجدول حتى 2030. بنفس الأجر الإجمالي، يصبح الصافي حوالي 10 483 درهماً في 2027 و10 617 درهماً في 2030. التفاصيل في مقال <a href="/ar/bareme-ir-maroc-2026-2030/">جدول الضريبة 2026-2030</a>، والحساب الشخصي عبر <a href="/simulateur/?lang=ar">المحاكي</a>.</p>
''' + SRC_AR},
},
{
 'id': 'smig', 'date': '2026-11-11',
 'slug': {'fr': '/smig-maroc-2026/', 'ar': '/ar/smig-maroc-2026/'},
 'title': {'fr': 'SMIG 2026 au Maroc : 17,92 DH de l’heure, brut et net mensuel | Salairi',
           'ar': 'الحد الأدنى للأجور SMIG 2026 بالمغرب: 17,92 درهماً للساعة، الأجر الإجمالي والصافي | Salairi'},
 'desc': {'fr': 'Montant du SMIG et du SMAG en 2026 au Maroc, calcul du salaire minimum mensuel brut et net (CNSS, AMO, IR) et règles à connaître.',
          'ar': 'مبلغ الحد الأدنى للأجور SMIG وSMAG في 2026 بالمغرب، حساب الأجر الأدنى الشهري الإجمالي والصافي، والقواعد التي يجب معرفتها.'},
 'h1': {'fr': 'SMIG 2026 au Maroc : combien en brut et en net ?', 'ar': 'الحد الأدنى للأجور 2026 بالمغرب: كم بالإجمالي وكم بالصافي؟'},
 'body': {
'fr': '''
<p>Depuis le <b>1er janvier 2026</b>, le salaire minimum interprofessionnel garanti (SMIG) des activités non agricoles est fixé à <b>17,92 DH brut de l’heure</b> (décret n° 2.25.983, Bulletin officiel n° 7469), soit une hausse de 5 % par rapport aux 17,10 DH de 2025. Dans l’agriculture, le SMAG est passé à <b>97,44 DH par jour</b> à partir du 1er avril 2026.</p>
<h2>Du taux horaire au salaire mensuel</h2>
<p>Le décret fixe un taux horaire. Pour un temps plein de 44 heures par semaine, on compte en pratique <b>191 heures par mois</b> : 17,92 × 191 = <b>3 422,72 DH brut</b> par mois. Certains employeurs utilisent 191,33 heures (44 h × 52 semaines ÷ 12), ce qui donne environ 3 429 DH.</p>
<h2>Du brut au net</h2>
<table><thead><tr><th>Ligne</th><th>Calcul</th><th>Montant</th></tr></thead><tbody>
<tr><td>Salaire brut</td><td>17,92 × 191 h</td><td>3 422,72 DH</td></tr>
<tr><td>CNSS</td><td>4,48 %</td><td>− 153,34 DH</td></tr>
<tr><td>AMO</td><td>2,26 %</td><td>− 77,35 DH</td></tr>
<tr><td>IR</td><td>net imposable ≈ 1 994 DH, sous le seuil</td><td>0 DH</td></tr>
<tr><td><b>Salaire net</b></td><td></td><td><b>≈ 3 192 DH</b></td></tr>
</tbody></table>
<p>Au niveau du SMIG, aucun impôt sur le revenu n’est dû : après les frais professionnels (35 %) et les cotisations, le revenu imposable reste bien en dessous de 3 333 DH par mois.</p>
<h2>Ce qu’il faut savoir</h2>
<ul>
<li>Le SMIG s’applique aux salariés du commerce, de l’industrie, des services et des professions libérales ; le SMAG au secteur agricole.</li>
<li>Les pourboires et les primes peuvent compter pour atteindre le minimum, mais pas les indemnités qui remboursent des frais.</li>
<li>Un travailleur payé à temps partiel touche au moins 17,92 DH par heure travaillée.</li>
<li>Les heures supplémentaires et la prime d’ancienneté s’ajoutent au minimum : voir nos guides sur les <a href="/heures-supplementaires-maroc/">heures supplémentaires</a> et la <a href="/prime-anciennete-maroc/">prime d’ancienneté</a>.</li>
</ul>
<p>Pour calculer un autre salaire, utilisez le <a href="/simulateur/?lang=fr">simulateur Salairi</a>.</p>
''' + SRC_FR,
'ar': '''
<p>منذ <b>فاتح يناير 2026</b>، حُدد الحد الأدنى القانوني للأجر (SMIG) في الأنشطة غير الفلاحية في <b>17,92 درهماً إجمالياً للساعة</b> (المرسوم رقم 2.25.983، الجريدة الرسمية عدد 7469)، أي بزيادة 5% مقارنة بـ17,10 دراهم في 2025. وفي القطاع الفلاحي، ارتفع SMAG إلى <b>97,44 درهماً لليوم</b> ابتداءً من فاتح أبريل 2026.</p>
<h2>من السعر بالساعة إلى الأجر الشهري</h2>
<p>يحدد المرسوم سعراً للساعة. بالنسبة لعمل كامل مدته 44 ساعة أسبوعياً، يُحتسب عملياً <b>191 ساعة شهرياً</b>: 17,92 × 191 = <b>3 422,72 درهماً إجمالياً</b> في الشهر. ويستعمل بعض المشغلين 191,33 ساعة (44 × 52 ÷ 12)، أي حوالي 3 429 درهماً.</p>
<h2>من الإجمالي إلى الصافي</h2>
<table><thead><tr><th>البند</th><th>الحساب</th><th>المبلغ</th></tr></thead><tbody>
<tr><td>الأجر الإجمالي</td><td>17,92 × 191 ساعة</td><td>3 422,72 درهماً</td></tr>
<tr><td>الضمان الاجتماعي</td><td>4,48%</td><td>− 153,34</td></tr>
<tr><td>التأمين الإجباري عن المرض</td><td>2,26%</td><td>− 77,35</td></tr>
<tr><td>الضريبة على الدخل</td><td>الدخل الخاضع ≈ 1 994 درهماً، دون العتبة</td><td>0</td></tr>
<tr><td><b>الأجر الصافي</b></td><td></td><td><b>≈ 3 192 درهماً</b></td></tr>
</tbody></table>
<p>في مستوى الحد الأدنى للأجر لا تُستحق أي ضريبة على الدخل: بعد المصاريف المهنية (35%) والاشتراكات، يبقى الدخل الخاضع أقل بكثير من 3 333 درهماً شهرياً.</p>
<h2>ما يجب معرفته</h2>
<ul>
<li>يطبق SMIG على أجراء التجارة والصناعة والخدمات والمهن الحرة، وSMAG على القطاع الفلاحي.</li>
<li>يمكن احتساب الحلوان والمنح لبلوغ الحد الأدنى، دون التعويضات التي تسدد مصاريف.</li>
<li>العامل بدوام جزئي يتقاضى على الأقل 17,92 درهماً عن كل ساعة عمل.</li>
<li>الساعات الإضافية ومنحة الأقدمية تضاف إلى الحد الأدنى: انظر دليلي <a href="/ar/heures-supplementaires-maroc/">الساعات الإضافية</a> و<a href="/ar/prime-anciennete-maroc/">منحة الأقدمية</a>.</li>
</ul>
<p>لحساب أجر آخر، استعمل <a href="/simulateur/?lang=ar">محاكي Salairi</a>.</p>
''' + SRC_AR},
},
{
 'id': 'anciennete', 'date': '2026-11-11',
 'slug': {'fr': '/prime-anciennete-maroc/', 'ar': '/ar/prime-anciennete-maroc/'},
 'title': {'fr': 'Prime d’ancienneté au Maroc : taux, calcul et exemples (Code du travail) | Salairi',
           'ar': 'منحة الأقدمية بالمغرب: النسب والحساب وأمثلة (مدونة الشغل) | Salairi'},
 'desc': {'fr': 'La prime d’ancienneté obligatoire dans le secteur privé au Maroc : 5 % après 2 ans jusqu’à 25 % après 25 ans, base de calcul, exemples chiffrés et traitement CNSS et IR.',
          'ar': 'منحة الأقدمية الإجبارية في القطاع الخاص بالمغرب: من 5% بعد سنتين إلى 25% بعد 25 سنة، أساس الحساب، أمثلة بالأرقام، والضمان الاجتماعي والضريبة.'},
 'h1': {'fr': 'Prime d’ancienneté : combien vous devez toucher', 'ar': 'منحة الأقدمية: كم يجب أن تتقاضى'},
 'body': {
'fr': '''
<p>Dans le secteur privé, le Code du travail (article 350) oblige l’employeur à verser une <b>prime d’ancienneté</b> dès que le salarié a passé deux ans dans l’entreprise. Elle augmente par paliers.</p>
<h2>Les taux légaux</h2>
<table><thead><tr><th>Ancienneté dans l’entreprise</th><th>Prime minimale</th></tr></thead><tbody>
<tr><td>moins de 2 ans</td><td>0 %</td></tr>
<tr><td>de 2 à 5 ans</td><td>5 %</td></tr>
<tr><td>de 5 à 12 ans</td><td>10 %</td></tr>
<tr><td>de 12 à 20 ans</td><td>15 %</td></tr>
<tr><td>de 20 à 25 ans</td><td>20 %</td></tr>
<tr><td>25 ans et plus</td><td>25 %</td></tr>
</tbody></table>
<p>Ce sont des minimums : une convention collective, le contrat ou l’usage de l’entreprise peuvent prévoir mieux.</p>
<h2>Sur quoi la calculer ?</h2>
<p>Le pourcentage s’applique au salaire effectivement perçu, en excluant notamment les heures supplémentaires, les indemnités qui remboursent des frais, les allocations familiales et les gratifications exceptionnelles. En pratique, la plupart des bulletins l’appliquent au <b>salaire de base</b>.</p>
<h2>Exemples</h2>
<ul>
<li>Salaire de base 6 000 DH, 3 ans d’ancienneté : 5 % → <b>300 DH</b> de prime par mois.</li>
<li>Salaire de base 6 000 DH, 13 ans d’ancienneté : 15 % → <b>900 DH</b> par mois.</li>
<li>Salaire au SMIG (3 422,72 DH), 6 ans d’ancienneté : 10 % → <b>342,27 DH</b> par mois.</li>
</ul>
<h2>Cotisations et impôt</h2>
<p>La prime d’ancienneté est un élément du salaire : elle est soumise à la CNSS (dans la limite du plafond de 6 000 DH), à l’AMO et à l’impôt sur le revenu. Une prime de 900 DH ne rapporte donc pas 900 DH nets : selon votre tranche d’IR, il en reste en général entre 610 et 840 DH.</p>
<h2>Et dans la fonction publique ?</h2>
<p>Il n’y a pas de prime d’ancienneté dans la fonction publique : l’ancienneté se traduit par l’avancement d’<b>échelon</b>, qui augmente l’indice et donc le traitement de base. Voir notre guide du <a href="/bulletin-paie-fonctionnaire-maroc/">bulletin de paie du fonctionnaire</a>.</p>
<p>Pour voir l’effet d’une prime sur votre net, ajoutez-la à votre salaire dans le <a href="/simulateur/?lang=fr">simulateur</a>.</p>
''' + SRC_FR,
'ar': '''
<p>في القطاع الخاص، تُلزم مدونة الشغل (المادة 350) المشغل بأداء <b>منحة الأقدمية</b> بمجرد قضاء الأجير سنتين في المقاولة، وترتفع على مراحل.</p>
<h2>النسب القانونية</h2>
<table><thead><tr><th>الأقدمية في المقاولة</th><th>المنحة الدنيا</th></tr></thead><tbody>
<tr><td>أقل من سنتين</td><td>0%</td></tr>
<tr><td>من 2 إلى 5 سنوات</td><td>5%</td></tr>
<tr><td>من 5 إلى 12 سنة</td><td>10%</td></tr>
<tr><td>من 12 إلى 20 سنة</td><td>15%</td></tr>
<tr><td>من 20 إلى 25 سنة</td><td>20%</td></tr>
<tr><td>25 سنة فأكثر</td><td>25%</td></tr>
</tbody></table>
<p>هذه حدود دنيا: يمكن لاتفاقية جماعية أو للعقد أو لعرف المقاولة أن تنص على أفضل منها.</p>
<h2>على أي أساس تُحسب؟</h2>
<p>تُطبق النسبة على الأجر المتقاضى فعلياً، مع استثناء الساعات الإضافية والتعويضات التي تسدد مصاريف والتعويضات العائلية والمكافآت الاستثنائية. عملياً، تطبقها أغلب أوراق الأداء على <b>الأجر الأساسي</b>.</p>
<h2>أمثلة</h2>
<ul>
<li>أجر أساسي 6 000 درهم وأقدمية 3 سنوات: 5% ← <b>300 درهم</b> شهرياً.</li>
<li>أجر أساسي 6 000 درهم وأقدمية 13 سنة: 15% ← <b>900 درهم</b> شهرياً.</li>
<li>أجر في مستوى الحد الأدنى (3 422,72 درهماً) وأقدمية 6 سنوات: 10% ← <b>342,27 درهماً</b> شهرياً.</li>
</ul>
<h2>الاشتراكات والضريبة</h2>
<p>منحة الأقدمية جزء من الأجر، فهي خاضعة للضمان الاجتماعي (في حدود سقف 6 000 درهم) وللتأمين الإجباري عن المرض وللضريبة على الدخل. لذلك فمنحة 900 درهم لا تعطي 900 درهم صافية: يبقى منها عادة بين 610 و840 درهماً حسب شريحة الضريبة.</p>
<h2>وفي الوظيفة العمومية؟</h2>
<p>لا توجد منحة أقدمية في الوظيفة العمومية: تُترجم الأقدمية بالترقي في <b>الرتبة</b>، مما يرفع الرقم الاستدلالي وبالتالي الراتب الأساسي. انظر دليل <a href="/ar/bulletin-paie-fonctionnaire-maroc/">ورقة أداء الموظف</a>.</p>
<p>لمعرفة أثر المنحة على صافيك، أضفها إلى أجرتك في <a href="/simulateur/?lang=ar">المحاكي</a>.</p>
''' + SRC_AR},
},
{
 'id': 'heures-sup', 'date': '2026-11-11',
 'slug': {'fr': '/heures-supplementaires-maroc/', 'ar': '/ar/heures-supplementaires-maroc/'},
 'title': {'fr': 'Heures supplémentaires au Maroc : majorations 25 %, 50 %, 100 % et calcul | Salairi',
           'ar': 'الساعات الإضافية بالمغرب: الزيادات 25% و50% و100% وطريقة الحساب | Salairi'},
 'desc': {'fr': 'Comment sont payées les heures supplémentaires dans le privé au Maroc : taux horaire, majorations de jour, de nuit et le jour de repos, exemple de calcul et impôt.',
          'ar': 'كيف تُؤدى الساعات الإضافية في القطاع الخاص بالمغرب: الأجر بالساعة، الزيادات نهاراً وليلاً ويوم الراحة، مثال للحساب، والضريبة.'},
 'h1': {'fr': 'Heures supplémentaires : comment elles sont payées', 'ar': 'الساعات الإضافية: كيف تُؤدى'},
 'body': {
'fr': '''
<p>Au Maroc, la durée légale du travail dans le secteur non agricole est de <b>44 heures par semaine</b> (ou 2 288 heures par an). Toute heure travaillée au-delà, à la demande de l’employeur, est une heure supplémentaire et doit être <b>majorée</b> (Code du travail, article 201).</p>
<h2>Les majorations</h2>
<table><thead><tr><th>Moment où l’heure est faite</th><th>Jour ouvrable</th><th>Jour de repos hebdomadaire</th></tr></thead><tbody>
<tr><td>entre 6 h et 21 h</td><td>+ 25 %</td><td>+ 50 %</td></tr>
<tr><td>entre 21 h et 6 h</td><td>+ 50 %</td><td>+ 100 %</td></tr>
</tbody></table>
<p>Dans le secteur agricole, les plages horaires sont de 5 h à 20 h et de 20 h à 5 h.</p>
<h2>Calculer le taux horaire</h2>
<p>Le taux horaire de base = salaire mensuel ÷ 191 heures. Pour un salaire de 7 640 DH : 7 640 ÷ 191 = <b>40 DH de l’heure</b>.</p>
<h2>Exemple</h2>
<p>Ce salarié fait dans le mois 8 heures supplémentaires en journée et 4 heures le vendredi soir après 21 h :</p>
<ul>
<li>8 h × 40 DH × 1,25 = <b>400 DH</b> ;</li>
<li>4 h × 40 DH × 1,50 = <b>240 DH</b> ;</li>
<li>total : <b>640 DH bruts</b> en plus du salaire.</li>
</ul>
<h2>Cotisations et impôt</h2>
<p>Les heures supplémentaires font partie du salaire brut : elles supportent la CNSS (dans la limite du plafond), l’AMO et l’IR. Elles peuvent faire passer une partie du salaire dans une tranche d’IR plus élevée ; pour connaître le net exact, ajoutez le montant brut dans le <a href="/simulateur/?lang=fr">simulateur</a>.</p>
<h2>À vérifier sur le bulletin</h2>
<ul>
<li>le nombre d’heures et le taux de majoration appliqué ;</li>
<li>les heures de nuit ou du jour de repos, majorées davantage ;</li>
<li>les heures ne doivent pas être remplacées par une « prime » forfaitaire inférieure à ce que donnerait le calcul légal.</li>
</ul>
<p>À lire aussi : <a href="/smig-maroc-2026/">SMIG 2026</a> et <a href="/prime-anciennete-maroc/">prime d’ancienneté</a>.</p>
''' + SRC_FR,
'ar': '''
<p>بالمغرب، المدة القانونية للعمل في القطاع غير الفلاحي هي <b>44 ساعة في الأسبوع</b> (أو 2 288 ساعة في السنة). كل ساعة يُشتغل فيها بعد ذلك بطلب من المشغل هي ساعة إضافية ويجب أن تُؤدى <b>بزيادة</b> (مدونة الشغل، المادة 201).</p>
<h2>نسب الزيادة</h2>
<table><thead><tr><th>توقيت الساعة</th><th>يوم عمل</th><th>يوم الراحة الأسبوعية</th></tr></thead><tbody>
<tr><td>بين 6 صباحاً و9 ليلاً</td><td>+ 25%</td><td>+ 50%</td></tr>
<tr><td>بين 9 ليلاً و6 صباحاً</td><td>+ 50%</td><td>+ 100%</td></tr>
</tbody></table>
<p>في القطاع الفلاحي، تكون الفترات من 5 صباحاً إلى 8 مساءً ومن 8 مساءً إلى 5 صباحاً.</p>
<h2>حساب الأجر بالساعة</h2>
<p>الأجر الأساسي بالساعة = الأجر الشهري ÷ 191 ساعة. لأجر قدره 7 640 درهماً: 7 640 ÷ 191 = <b>40 درهماً للساعة</b>.</p>
<h2>مثال</h2>
<p>اشتغل هذا الأجير خلال الشهر 8 ساعات إضافية نهاراً و4 ساعات ليلة الجمعة بعد التاسعة:</p>
<ul>
<li>8 × 40 × 1,25 = <b>400 درهم</b>؛</li>
<li>4 × 40 × 1,50 = <b>240 درهماً</b>؛</li>
<li>المجموع: <b>640 درهماً إجمالياً</b> إضافة إلى الأجر.</li>
</ul>
<h2>الاشتراكات والضريبة</h2>
<p>الساعات الإضافية جزء من الأجر الإجمالي: تخضع للضمان الاجتماعي (في حدود السقف) والتأمين الإجباري عن المرض والضريبة على الدخل، وقد تنقل جزءاً من الأجر إلى شريحة ضريبية أعلى. لمعرفة الصافي بدقة، أضف المبلغ الإجمالي في <a href="/simulateur/?lang=ar">المحاكي</a>.</p>
<h2>ما يجب التحقق منه في ورقة الأداء</h2>
<ul>
<li>عدد الساعات ونسبة الزيادة المطبقة؛</li>
<li>ساعات الليل أو يوم الراحة التي تُزاد بنسبة أعلى؛</li>
<li>ألا تُعوَّض الساعات بـ«منحة» جزافية أقل مما يعطيه الحساب القانوني.</li>
</ul>
<p>اقرأ أيضاً: <a href="/ar/smig-maroc-2026/">الحد الأدنى للأجور 2026</a> و<a href="/ar/prime-anciennete-maroc/">منحة الأقدمية</a>.</p>
''' + SRC_AR},
},
{
 'id': 'glossaire', 'date': '2026-11-11',
 'slug': {'fr': '/glossaire-bulletin-de-paie-francais-arabe/', 'ar': '/ar/glossaire-bulletin-de-paie-francais-arabe/'},
 'title': {'fr': 'Glossaire du bulletin de paie français-arabe (Maroc) : 30 termes expliqués | Salairi',
           'ar': 'معجم ورقة الأداء فرنسي-عربي (المغرب): 30 مصطلحاً مشروحاً | Salairi'},
 'desc': {'fr': 'Traitement de base, indemnité de résidence, échelon, net imposable, CMR, AMO… les termes du bulletin de paie marocain en français et en arabe, avec une explication simple.',
          'ar': 'الراتب الأساسي، تعويض الإقامة، الرتبة، الدخل الخاضع، الصندوق المغربي للتقاعد، التأمين… مصطلحات ورقة الأداء بالمغرب بالفرنسية والعربية مع شرح مبسط.'},
 'h1': {'fr': 'Glossaire du bulletin de paie : français – arabe', 'ar': 'معجم ورقة الأداء: فرنسي – عربي'},
 'body': {},
},
]

_TERMS = [
 ('Salaire brut', 'الأجر الإجمالي', 'Total avant cotisations et impôt.', 'المجموع قبل الاشتراكات والضريبة.'),
 ('Salaire net', 'الأجر الصافي', 'Ce qui est versé sur votre compte.', 'ما يُحوَّل إلى حسابك.'),
 ('Salaire net imposable', 'الدخل الصافي الخاضع للضريبة', 'Base de calcul de l’IR, après frais professionnels et cotisations.', 'أساس حساب الضريبة بعد المصاريف المهنية والاشتراكات.'),
 ('Salaire de base', 'الأجر الأساسي', 'Salaire du contrat, hors primes et indemnités (privé).', 'أجر العقد دون المنح والتعويضات (القطاع الخاص).'),
 ('Traitement de base', 'الراتب الأساسي', 'Salaire du fonctionnaire calculé à partir de l’indice.', 'راتب الموظف المحسوب انطلاقاً من الرقم الاستدلالي.'),
 ('Indice', 'الرقم الاستدلالي', 'Nombre de points fixé par le grade et l’échelon.', 'عدد النقط المحدد حسب الدرجة والرتبة.'),
 ('Échelle', 'السلم', 'Niveau du cadre dans la grille de la fonction publique.', 'مستوى الإطار في شبكة الوظيفة العمومية.'),
 ('Grade', 'الدرجة', 'Position dans le cadre (1er grade, 2e grade, principal…).', 'الموقع داخل الإطار (الدرجة الأولى، الثانية، الممتازة…).'),
 ('Échelon', 'الرتبة', 'Ancienneté dans le grade ; chaque échelon augmente l’indice.', 'الأقدمية داخل الدرجة؛ كل رتبة ترفع الرقم الاستدلالي.'),
 ('Hors échelle', 'خارج السلم', 'Grades supérieurs à l’échelle 11.', 'الدرجات الأعلى من السلم 11.'),
 ('Corps', 'الهيئة', 'Ensemble de fonctionnaires d’un même statut.', 'مجموعة موظفين يخضعون لنفس النظام الأساسي.'),
 ('Cadre', 'الإطار', 'Métier au sein du corps (administrateur, ingénieur, professeur…).', 'المهنة داخل الهيئة (متصرف، مهندس، أستاذ…).'),
 ('Indemnité de résidence', 'تعويض الإقامة', 'Pourcentage du traitement selon la zone A, B ou C.', 'نسبة من الراتب حسب المنطقة أ أو ب أو ج.'),
 ('Indemnité de sujétion', 'تعويض عن التبعات', 'Indemnité liée aux contraintes du poste.', 'تعويض مرتبط بإكراهات المنصب.'),
 ('Indemnité d’encadrement', 'تعويض التأطير', 'Indemnité des cadres et responsables.', 'تعويض الأطر والمسؤولين.'),
 ('Indemnité de technicité', 'تعويض عن التقنية', 'Indemnité de certains corps techniques.', 'تعويض بعض الهيئات التقنية.'),
 ('Allocations familiales', 'التعويضات العائلية', 'Montant versé pour chaque enfant à charge.', 'مبلغ يُؤدى عن كل طفل في الكفالة.'),
 ('Prime d’ancienneté', 'منحة الأقدمية', '5 % à 25 % du salaire selon l’ancienneté (privé).', 'من 5% إلى 25% من الأجر حسب الأقدمية (الخاص).'),
 ('Heures supplémentaires', 'الساعات الإضافية', 'Heures au-delà de 44 h par semaine, majorées.', 'الساعات بعد 44 ساعة أسبوعياً، تُؤدى بزيادة.'),
 ('Indemnité de transport', 'تعويض النقل', 'Indemnité exonérée dans certaines limites.', 'تعويض معفى في حدود معينة.'),
 ('Indemnité de panier', 'تعويض السلة', 'Indemnité de repas, exonérée dans certaines limites.', 'تعويض الوجبة، معفى في حدود معينة.'),
 ('CNSS', 'الصندوق الوطني للضمان الاجتماعي', 'Cotisation sociale des salariés du privé (4,48 % plafonnés).', 'اشتراك أجراء القطاع الخاص (4,48% بسقف).'),
 ('AMO', 'التأمين الإجباري الأساسي عن المرض', 'Assurance maladie obligatoire.', 'التأمين الصحي الإجباري.'),
 ('CMR', 'الصندوق المغربي للتقاعد', 'Caisse de retraite des fonctionnaires (14 %).', 'صندوق تقاعد الموظفين (14%).'),
 ('CIMR', 'الصندوق المهني المغربي للتقاعد', 'Retraite complémentaire facultative du privé.', 'تقاعد تكميلي اختياري في القطاع الخاص.'),
 ('Mutuelle', 'التعاضدية', 'Couverture santé complémentaire (MGEN, MGPAP…).', 'تغطية صحية تكميلية (MGEN، MGPAP…).'),
 ('Fondation des œuvres sociales', 'مؤسسة الأعمال الاجتماعية', 'Cotisation volontaire selon le ministère.', 'اشتراك طوعي حسب الوزارة.'),
 ('Frais professionnels', 'المصاريف المهنية', 'Déduction forfaitaire avant le calcul de l’IR.', 'خصم جزافي قبل حساب الضريبة.'),
 ('IR (impôt sur le revenu)', 'الضريبة على الدخل', 'Impôt retenu à la source chaque mois.', 'ضريبة تُقتطع من المنبع كل شهر.'),
 ('Personnes à charge', 'الأشخاص في الكفالة', 'Réduction d’IR de 50 DH par mois chacune (6 au maximum).', 'تخفيض الضريبة بـ50 درهماً شهرياً عن كل واحد (6 كحد أقصى).'),
]
_rows_fr = ''.join(f'<tr><td><b>{a}</b></td><td dir="rtl" lang="ar">{b}</td><td>{c}</td></tr>' for a, b, c, d in _TERMS)
_rows_ar = ''.join(f'<tr><td><b>{b}</b></td><td dir="ltr" lang="fr">{a}</td><td>{d}</td></tr>' for a, b, c, d in _TERMS)
ARTICLES2[-1]['body'] = {
 'fr': '<p>Les bulletins de paie au Maroc mélangent souvent le français et l’arabe. Voici les 30 termes les plus courants, avec leur équivalent et ce qu’ils signifient.</p>'
       f'<table><thead><tr><th>Français</th><th>العربية</th><th>Signification</th></tr></thead><tbody>{_rows_fr}</tbody></table>'
       '<p>Pour voir ces lignes appliquées à votre cas, lisez <a href="/bulletin-paie-fonctionnaire-maroc/">comprendre son bulletin de fonctionnaire</a> ou <a href="/calcul-ir-salaire-maroc/">calculer l’IR pas à pas</a>.</p>' + SRC_FR,
 'ar': '<p>تمزج أوراق الأداء بالمغرب غالباً بين الفرنسية والعربية. إليك 30 مصطلحاً هي الأكثر تداولاً، مع ما يقابلها ومعناها.</p>'
       f'<table><thead><tr><th>العربية</th><th>Français</th><th>المعنى</th></tr></thead><tbody>{_rows_ar}</tbody></table>'
       '<p>لرؤية هذه البنود مطبقة على حالتك، اقرأ <a href="/ar/bulletin-paie-fonctionnaire-maroc/">فهم ورقة أداء الموظف</a> أو <a href="/ar/calcul-ir-salaire-maroc/">حساب الضريبة خطوة بخطوة</a>.</p>' + SRC_AR,
}
