
<div align="center">
  <img src="https://github.com/user-attachments/assets/8ddfb7dc-e265-4f7b-913f-1f23ca0b4fcd" alt="شكل البرنامج وهو شغال" width="350" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 1px solid #ccc;">
</div>
<div dir="rtl" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                      padding: 30px; 
                      border-radius: 20px; 
                      color: #2d3436; 
                      line-height: 1.8; 
                      box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
                      max-width: 800px; 
                      margin: 20px auto; 
                      border: 1px solid rgba(255,255,255,0.3);">

  <h1 style="color: #0984e3; border-bottom: 3px solid #74b9ff; padding-bottom: 10px; display: inline-block;">
    وصف البرنامج: نظام حساب الخصومات الذكي 📝
  </h1>

  <section style="margin-top: 25px; background: rgba(255,255,255,0.5); padding: 15px; border-radius: 12px;">
    <h2 style="color: #2d3436; font-size: 1.4em;">🎯 الهدف من الكود</h2>
    <p style="font-size: 1.1em; margin-right: 10px;">
      حساب قيمة الخصم المستحق على فاتورة المشتريات بناءً على قيمة المبلغ الإجمالية، مع إضافة <b>"بونص"</b> تشجيعي في حالات خاصة. 📈
    </p>
  </section>

  <h2 style="color: #2d3436; margin-top: 30px; font-size: 1.4em;">⚙️ خطوات عمل البرنامج</h2>
  
  <ul style="list-style-type: none; padding-right: 0;">
    <li style="background: #ffffff; margin-bottom: 10px; padding: 15px; border-radius: 10px; border-right: 5px solid #00cec9; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
      <b>1. استقبال البيانات:</b> يبدأ البرنامج بطلب إدخال قيمة الفاتورة وتحويلها لرقم عشري <code>float</code>. 💰
    </li>
    <li style="background: #ffffff; margin-bottom: 10px; padding: 15px; border-radius: 10px; border-right: 5px solid #6c5ce7; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
      <b>2. التحقق الأولي:</b> يختبر البرنامج ما إذا كانت الفاتورة <b>رقماً زوجياً وأكبر من 50</b> لإعطاء رسالة بونص. 🎊
    </li>
    <li style="background: #ffffff; margin-bottom: 10px; padding: 15px; border-radius: 10px; border-right: 5px solid #fdcb6e; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
      <b>3. الشرائح الضريبية:</b>
      <ul style="margin-top: 10px; list-style-type: circle; margin-right: 20px;">
        <li>فوق <b>100</b>: خصم <span style="color: #d63031; font-weight: bold;">20%</span> 🥇</li>
        <li>بين <b>50 و 100</b>: خصم <span style="color: #e17055; font-weight: bold;">10%</span> 🥈</li>
        <li>أقل من <b>50</b>: لا يوجد خصم 🚫</li>
      </ul>
    </li>
    <li style="background: #ffffff; margin-bottom: 10px; padding: 15px; border-radius: 10px; border-right: 5px solid #00b894; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
      <b>4. البونص الإضافي:</b> إضافة <b>5% إضافية</b> لو تحقق شرط الرقم الزوجي (تراكمي). 🎁
    </li>
    <li style="background: #ffffff; margin-bottom: 10px; padding: 15px; border-radius: 10px; border-right: 5px solid #0984e3; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
      <b>5. النتائج النهائية:</b> عرض المبلغ النهائي بدقة <code>.2f</code>. 🧮
    </li>
  </ul>

  <div style="margin-top: 30px; background: #dfe6e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2d3436; font-style: italic;">
    <strong>💡 ملاحظة تقنية:</strong> الكود يستخدم جمل <code>if-elif-else</code> للشرائح، وجملة <code>if</code> منفصلة للبونص لضمان <b>تراكم الخصم</b>.
  </div>

</div>
