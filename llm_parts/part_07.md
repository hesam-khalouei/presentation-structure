# Project Source Code (Part 7)

این فایل شامل کد پروژه است. هر فایل با `=== path ===` مشخص شده و کد داخل بلوک ```lang``` است. base64 فونت/تصویر حذف شده.

---

=== ./slides/slide-02-ecosystem.html ===

```html
<section
  class="slide active"
  data-chapter="0"
  data-title="اکوسیستم همراه اول و شرکت‌های کلیدی">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل اول · پشتوانه راهبردی</span>
      <span style="font-size: 12px; color: var(--text-muted)"
        >زنجیره یکپارچه ارتباطات، فناوری، خدمات دیجیتال و مالی</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      اکوسیستم <span class="accent-green">همراه اول</span>؛ بزرگ‌ترین اپراتور
      ارتباطی و دیجیتال کشور
    </h2>

    <p class="slide-subtitle anim-up delay-2">
      همراه اول با تکیه بر مجموعه‌ای از شرکت‌ها و کسب‌وکارهای تخصصی، زنجیره‌ای
      گسترده از خدمات ارتباطی، دیجیتال، فناوری و مالی را توسعه داده است.
    </p>

    <div class="ecosystem-layout anim-up delay-3">
      <!-- ۱۲ شرکت کلیدی -->
      <div class="glass-card ecosystem-companies-card">
        <div class="ecosystem-card-header">
          <h3>۱۲ شرکت کلیدی اکوسیستم همراه اول</h3>
          <span class="ecosystem-card-header-badge"
            >بازوهای اجرایی و تخصصی</span
          >
        </div>

        <div class="companies-grid">
          <div class="company-pill featured-ebcom">
            <span class="comp-logo-box"
              ><img
                src=".././assets/images/logos/partners/ebcom.svg"
                alt="EBCOM"
            /></span>
            <span class="comp-name">EBCOM</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box"
              ><img src="./assets/nak.png" alt="نقش اول کیفیت"
            /></span>
            <span class="comp-name">نقش اول کیفیت</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box"
              ><img src="./assets/mobinnet.svg" alt="مبین‌نت"
            /></span>
            <span class="comp-name">مبین‌نت</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box"
              ><img src="./assets/mci.svg" alt="همراه اول"
            /></span>
            <span class="comp-name">همراه اول</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box"
              ><img src="./assets/behsa.png" alt="بهسا"
            /></span>
            <span class="comp-name">بهسا</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box"
              ><img src="./assets/hub.png" alt="هاب هوشمند"
            /></span>
            <span class="comp-name">هاب هوشمند</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box"
              ><img src="./assets/ebcom.svg" alt="ستاره اول"
            /></span>
            <span class="comp-name">ستاره اول</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="روبیکا"
            /></span>
            <span class="comp-name">روبیکا</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="توسعه نور دنا"
            /></span>
            <span class="comp-name">توسعه نور دنا</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="حرکت اول"
            /></span>
            <span class="comp-name">حرکت اول</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="آرمان"
            /></span>
            <span class="comp-name">آرمان</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="جیرینگ"
            /></span>
            <span class="comp-name">جیرینگ</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="پارسا شریف"
            /></span>
            <span class="comp-name">پارسا شریف</span>
          </div>
          <div class="company-pill">
            <span class="comp-logo-box placeholder-logo"
              ><img src="./assets/ebcom.svg" alt="افرانت"
            /></span>
            <span class="comp-name">افرانت</span>
          </div>
        </div>

        <!-- ۷ سرویس دیجیتال -->
        <div class="ecosystem-services-footer">
          <div class="ecosystem-services-title">
            سرویس‌های دیجیتال شاخص شرکت همراه اول:
          </div>
          <div class="ecosystem-services-list">
            <span class="service-pill service-pill-featured"
              >اوانو (Ewano)</span
            >
            <span class="service-pill">ستاره یک</span>
            <span class="service-pill">ذره‌بین</span>
            <span class="service-pill">همراه من</span>
            <span class="service-pill">شاد</span>
            <span class="service-pill">بومینو</span>
            <span class="service-pill">روبیکا</span>
          </div>
        </div>
      </div>

      <!-- نمودار مداری SVG -->
      <div class="glass-card no-collapse s2-diagram-card">
        <svg class="s2-diagram-svg" viewBox="0 0 540 435">
          <defs>
            <radialGradient id="mciCore2" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#00D4B4"></stop>
              <stop offset="100%" stop-color="#007A66"></stop>
            </radialGradient>
          </defs>

          <!-- مدار بیرونی -->
          <circle
            cx="270"
            cy="218"
            r="185"
            fill="none"
            stroke="rgba(0,212,180,0.25)"
            stroke-width="2"
            class="svg-flow-line"></circle>
          <!-- مدار درونی -->
          <circle
            cx="270"
            cy="218"
            r="118"
            fill="none"
            stroke="rgba(255,119,34,0.32)"
            stroke-width="2"
            stroke-dasharray="6 6"></circle>

          <!-- خطوط اتصال -->
          <line
            x1="270"
            y1="218"
            x2="270"
            y2="35"
            stroke="rgba(0,212,180,0.4)"
            stroke-width="2.5"></line>
          <line
            x1="270"
            y1="218"
            x2="435"
            y2="128"
            stroke="rgba(255,255,255,0.18)"
            stroke-width="2"></line>
          <line
            x1="270"
            y1="218"
            x2="435"
            y2="308"
            stroke="rgba(255,255,255,0.18)"
            stroke-width="2"></line>
          <line
            x1="270"
            y1="218"
            x2="105"
            y2="128"
            stroke="rgba(255,255,255,0.18)"
            stroke-width="2"></line>
          <line
            x1="270"
            y1="218"
            x2="105"
            y2="308"
            stroke="rgba(255,255,255,0.18)"
            stroke-width="2"></line>
          <line
            x1="270"
            y1="218"
            x2="270"
            y2="400"
            stroke="rgba(255,119,34,0.4)"
            stroke-width="2.5"></line>

          <!-- هسته مرکزی -->
          <circle
            cx="270"
            cy="218"
            r="70"
            fill="url(#mciCore2)"
            class="svg-pulse"></circle>
          <text
            x="270"
            y="213"
            text-anchor="middle"
            fill="#0B0F13"
            font-size="20"
            font-weight="900">
            همراه اول
          </text>
          <text
            x="270"
            y="238"
            text-anchor="middle"
            fill="#0B0F13"
            font-size="14"
            font-weight="800">
            MCI Ecosystem
          </text>

          <!-- گره بالا: EBCOM -->
          <rect
            x="180"
            y="10"
            width="180"
            height="50"
            rx="25"
            fill="#00D4B4"
            stroke="#FFFFFF"
            stroke-width="1.5"></rect>
          <text
            x="270"
            y="40"
            text-anchor="middle"
            fill="#0B0F13"
            font-size="17"
            font-weight="900">
            EBCOM (فین‌تک)
          </text>

          <!-- گره پایین: اوانو -->
          <rect
            x="180"
            y="375"
            width="180"
            height="50"
            rx="25"
            fill="#FF7722"
            stroke="#FFFFFF"
            stroke-width="1.5"></rect>
          <text
            x="270"
            y="402"
            text-anchor="middle"
            fill="#FFFFFF"
            font-size="17"
            font-weight="900">
            پلتفرم اوانو
          </text>

          <!-- گره بالا-راست: ارتباطات و ابری -->
          <rect
            x="355"
            y="102"
            width="165"
            height="48"
            rx="24"
            fill="#171F26"
            stroke="#00D4B4"
            stroke-width="1.5"></rect>
          <text
            x="437"
            y="128"
            text-anchor="middle"
            fill="#FFFFFF"
            font-size="15"
            font-weight="800">
            ارتباطات و ابری
          </text>

          <!-- گره پایین-راست: مالی و پرداخت -->
          <rect
            x="355"
            y="284"
            width="165"
            height="48"
            rx="24"
            fill="#171F26"
            stroke="#00D4B4"
            stroke-width="1.5"></rect>
          <text
            x="437"
            y="311"
            text-anchor="middle"
            fill="#FFFFFF"
            font-size="15"
            font-weight="800">
            مالی و پرداخت
          </text>

          <!-- گره بالا-چپ: پلتفرم‌های دیجیتال -->
          <rect
            x="20"
            y="102"
            width="170"
            height="48"
            rx="24"
            fill="#171F26"
            stroke="#00D4B4"
            stroke-width="1.5"></rect>
          <text
            x="105"
            y="128"
            text-anchor="middle"
            fill="#FFFFFF"
            font-size="15"
            font-weight="800">
            پلتفرم‌های دیجیتال
          </text>

          <!-- گره پایین-چپ: زیرساخت سازمانی -->
          <rect
            x="20"
            y="284"
            width="170"
            height="48"
            rx="24"
            fill="#171F26"
            stroke="#00D4B4"
            stroke-width="1.5"></rect>
          <text
            x="105"
            y="311"
            text-anchor="middle"
            fill="#FFFFFF"
            font-size="15"
            font-weight="800">
            زیرساخت سازمانی
          </text>
        </svg>

        <div class="s2-diagram-caption">
          پشتوانه تامین سرمایه، زیرساخت ارتباطی و شبکه مالی در مقیاس ملی
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-17-overcharge.html ===

```html
<section
  class="slide"
  data-chapter="3"
  data-title="مدل‌های ارائه اوورشارژ رفاهیات سازمانی">
  <div class="slide-inner">
    <!-- ── هدر اسلاید ── -->
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل چهارم · الگوهای تخصیص اعتبار و مزایای سازمانی</span
      >
      <span class="slide-top-meta-formula"
        >انعطاف کامل متناسب با فرآیندهای مالی و بودجه‌ای سازمان شما</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      مدل‌های ارائه <span class="accent-green">اوور شارژ رفاهیات</span> به پرسنل
    </h2>

    <!-- ── گرید اصلی: ۳ کارت تخصیص + استیج ووچر ── -->
    <div class="grid-2 anim-up delay-3 s17-models-grid">
      <!-- ستون راست: ۳ کارت تخصیص -->
      <div class="s17-alloc-stack">
        <!-- کارت ۱: شارژ مستقیم -->
        <div class="glass-card s17-alloc-card border-right-green">
          <div class="s17-alloc-head">
            <div class="s17-alloc-num s17-num-green">۱</div>
            <h3 class="s17-alloc-title text-green">شارژ مستقیم پرسنل</h3>
          </div>
          <p class="s17-alloc-text">
            تخصیص مستقیم اوور شارژ رفاهی به کیف پول تک‌تک کارکنان سازمان بر اساس
            لیست و سرفصل‌های تعیین‌شده توسط منابع انسانی.
          </p>
          <div class="s17-alloc-foot s17-foot-green">
            ✓ فعال‌سازی آنی + ارسال پیامک اطلاع‌رسانی به هر کارمند
          </div>
        </div>

        <!-- کارت ۲: کیف پول تجمیعی -->
        <div class="glass-card s17-alloc-card border-right-orange">
          <div class="s17-alloc-head">
            <div class="s17-alloc-num s17-num-orange">۲</div>
            <h3 class="s17-alloc-title text-orange">کیف پول تجمیعی</h3>
          </div>
          <p class="s17-alloc-text">
            تخصیص اوور شارژ در کیف پول مدیران واحدها یا افراد رابط تعیین‌شده از
            سوی سازمان برای خریدهای گروهی و مدیریت بودجه بخش‌ها.
          </p>
          <div class="s17-alloc-foot s17-foot-orange">
            ✓ مدیریت متمرکز تنخواه‌های رفاهی و پذیرایی شعب
          </div>
        </div>

        <!-- کارت ۳: ووچرکارت -->
        <div class="glass-card s17-alloc-card border-right-sky">
          <div class="s17-alloc-head">
            <div class="s17-alloc-num s17-num-sky">۳</div>
            <h3 class="s17-alloc-title text-sky">ووچرکارت (گیفت‌کارت)</h3>
          </div>
          <p class="s17-alloc-text">
            ارائه ووچرکارت‌های فیزیکی و دیجیتال بی‌نام برای تخصیص انعطاف‌پذیر
            مزایا، پاداش‌های مناسبتی و هدایای درون و برون‌سازمانی.
          </p>
          <div class="s17-alloc-foot s17-foot-sky">
            ✓ قابل اهدا به پرسنل، مهمانان سازمانی و شرکای تجاری
          </div>
        </div>
      </div>

      <!-- ستون چپ: استیج ووچرکارت‌ها (Click to Flip) -->
      <div class="voucher-vertical-stage">
        <!-- کارت ۳ میلیون تومان (سمت راست) -->
        <div
          class="voucher-card-item vc-card-1"
          onclick="toggleVoucherFlip(this)"
          title="برای مشاهده پشت کارت کلیک کنید">
          <div class="vcard-inner">
            <div class="vcard-side vcard-front">
              <img
                src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..._CARD_3M_FRONT"
                alt="ووچر کارت ۳ میلیون تومان" />
            </div>
            <div class="vcard-side vcard-back">
              <img
                src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..._CARD_3M_BACK"
                alt="پشت ووچر کارت ۳ میلیون تومان" />
            </div>
          </div>
        </div>

        <!-- کارت ۵ میلیون تومان (وسط) -->
        <div
          class="voucher-card-item vc-card-2"
          onclick="toggleVoucherFlip(this)"
          title="برای مشاهده پشت کارت کلیک کنید">
          <div class="vcard-inner">
            <div class="vcard-side vcard-front">
              <img
                src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..._CARD_5M_FRONT"
                alt="ووچر کارت ۵ میلیون تومان" />
            </div>
            <div class="vcard-side vcard-back">
              <img
                src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..._CARD_5M_BACK"
                alt="پشت ووچر کارت ۵ میلیون تومان" />
            </div>
          </div>
        </div>

        <!-- کارت ۱۰ میلیون تومان (سمت چپ) -->
        <div
          class="voucher-card-item vc-card-3"
          onclick="toggleVoucherFlip(this)"
          title="برای مشاهده پشت کارت کلیک کنید">
          <div class="vcard-inner">
            <div class="vcard-side vcard-front">
              <img
                src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..._CARD_10M_FRONT"
                alt="ووچر کارت ۱۰ میلیون تومان" />
            </div>
            <div class="vcard-side vcard-back">
              <img
                src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..._CARD_10M_BACK"
                alt="پشت ووچر کارت ۱۰ میلیون تومان" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-04-services.html ===

```html
<section
  class="slide active"
  data-chapter="0"
  data-title="خدمات اوانو در یک نگاه (۱۰ حوزه کلیدی)">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل اول · سوپراپلیکیشن جامع</span>
      <span class="slide-top-meta-hint"
        >پوشش کامل نیازهای روزمره، مالی و سبک زندگی کارکنان</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      خدمات <span class="accent-green">اوانو</span> در یک نگاه؛ ۱۰ حوزه خدماتی
      در یک سوپراپ
    </h2>

    <div class="s4-services-grid anim-up delay-3">
      <div class="s4-service-tile active">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <rect x="2" y="5" width="20" height="14" rx="2"></rect>
            <line x1="2" y1="10" x2="22" y2="10"></line>
          </svg>
        </div>
        <h4>۱. خدمات بانکی و مالی</h4>
        <p>کارت‌به‌کارت، کیف پول، موجودی و خدمات بانکی</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <rect x="5" y="2" width="14" height="20" rx="2"></rect>
            <line x1="12" y1="18" x2="12.01" y2="18"></line>
          </svg>
        </div>
        <h4>۲. خدمات اپراتوری</h4>
        <p>خرید شارژ، بسته اینترنت و پرداخت قبوض</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
          </svg>
        </div>
        <h4>۳. خدمات بیمه</h4>
        <p>استعلام، مقایسه و خرید انواع بیمه‌نامه</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <circle cx="9" cy="21" r="1"></circle>
            <circle cx="20" cy="21" r="1"></circle>
            <path
              d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
          </svg>
        </div>
        <h4>۴. خدمات فروشگاهی</h4>
        <p>خرید آنلاین و حضوری از ۹٬۴۱۵ پذیرنده</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path
              d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path>
          </svg>
        </div>
        <h4>۵. سفر و گردشگری</h4>
        <p>بلیط پرواز، قطار، اتوبوس و رزرو هتل و اقامتگاه</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path
              d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
        </div>
        <h4>۶. نیکوکاری (همراه مهربانی)</h4>
        <p>مشارکت در پویش‌های خیرخواهانه و مسئولیت اجتماعی</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
          </svg>
        </div>
        <h4>۷. خدمات سلامتی</h4>
        <p>نوبت‌دهی پزشک، مشاوره آنلاین و خدمات داروخانه</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
          </svg>
        </div>
        <h4>۸. آموزش و توسعه فردی</h4>
        <p>دوره‌های آموزشی، کتاب صوتی و الکترونیک</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path
              d="M14 16H9m10 0h3v-3.15a1 1 0 0 0-.84-.99L16 11l-2.7-3.6a1 1 0 0 0-.8-.4H5.24a2 2 0 0 0-1.8 1.1l-.8 1.63A6 6 0 0 0 2 12.42V16h2"></path>
            <circle cx="6.5" cy="16.5" r="2.5"></circle>
            <circle cx="16.5" cy="16.5" r="2.5"></circle>
          </svg>
        </div>
        <h4>۹. خدمات خودرویی</h4>
        <p>عوارض آزادراهی، طرح ترافیک و خلافی خودرو</p>
      </div>

      <div class="s4-service-tile">
        <div class="service-icon-box">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2">
            <path d="M3 21h18"></path>
            <path d="M5 21V7l8-4v18"></path>
            <path d="M19 21V11l-6-4"></path>
          </svg>
        </div>
        <h4>۱۰. خدمات شهروندی</h4>
        <p>شارژ کارت بلیت مترو و اتوبوس و خدمات شهری</p>
      </div>
    </div>
  </div>
</section>
```

=== ./components/footer.html ===

```html
<footer class="deck-footer">
  <div class="progress-track">
    <div class="progress-fill" id="progressFill"></div>
  </div>

  <div class="nav-controls">
    <button class="nav-arrow-btn" id="prevBtn" onclick="prevSlide()">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <line x1="5" y1="12" x2="19" y2="12"/>
        <polyline points="12 5 19 12 12 19"/>
      </svg>
      <span>اسلاید قبلی</span>
    </button>
    <div class="slide-counter-pill">
      <span>اسلاید</span>
      <strong id="currentSlideNum" class="text-green">۱</strong>
      <span>از</span>
      <strong id="totalSlideNum">۲۱</strong>
    </div>
    <button class="nav-arrow-btn" id="nextBtn" onclick="nextSlide()">
      <span>اسلاید بعدی</span>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <line x1="19" y1="12" x2="5" y2="12"/>
        <polyline points="12 19 5 12 12 5"/>
      </svg>
    </button>
  </div>

  <div class="slide-dots" id="slideDots"></div>

  <div class="text-xs text-muted flex flex-gap-12">
    <span>راهنما: <kbd class="bg-glass text-white rounded" style="padding:2px 6px;">←</kbd> <kbd class="bg-glass text-white rounded" style="padding:2px 6px;">→</kbd> یا <kbd class="bg-glass text-white rounded" style="padding:2px 6px;">Space</kbd></span>
  </div>
</footer>
```

=== ./components/drawer.html ===

```html
<div class="drawer-backdrop" id="drawerBackdrop" onclick="if(event.target===this) toggleDrawer()">
  <div class="drawer-panel">
    <div class="flex-between" style="padding-bottom:14px; border-bottom:1px solid var(--border-glass);">
      <h3 class="text-lg font-black text-white">فهرست اسلایدهای پرزنتیشن</h3>
      <button class="icon-btn" onclick="toggleDrawer()">✕ بستن</button>
    </div>
    <div id="drawerList" class="flex-col flex-gap-8"></div>
  </div>
</div>
```

=== ./components/header.html ===

```html
<!-- محتوای header -->
<header class="deck-header">
  <div class="brand-cluster flex flex-gap-20">
    <div class="header-ewano-logo" onclick="goToSlide(0)" title="اوانو">
      <img src="assets/images/logos/partners/ewano.svg" alt="Ewano" style="height:44px; width:auto; border-radius:10px; display:block;">
    </div>
    <div class="header-partner-logos flex flex-gap-16" style="padding-right:16px; border-right:1px solid rgba(255,255,255,0.15);">
      <img src="assets/images/logos/partners/ebcom.svg" alt="EBCOM" title="همراه کسب‌وکارهای هوشمند (EBCOM)" style="height:28px; width:auto; display:block;">
      <span style="display:inline-block; width:1px; height:24px; background:rgba(255,255,255,0.18);"></span>
      <img src="assets/images/logos/partners/mci.svg" alt="MCI" title="همراه اول" style="height:28px; width:auto; display:block;">
    </div>
  </div>

  <nav class="chapter-nav" id="chapterNav">
    <button class="chapter-btn active" onclick="goToSlide(0)">۱. اکوسیستم و اوانو</button>
    <button class="chapter-btn" onclick="goToSlide(5)">۲. دمو و ماشین‌حساب</button>
    <button class="chapter-btn" onclick="goToSlide(10)">۳. مسیر ۶ مرحله‌ای اعتبار</button>
    <button class="chapter-btn" onclick="goToSlide(15)">۴. رفاهیات و راهکار نقدی</button>
    <button class="chapter-btn" onclick="goToSlide(19)">۵. شبکه پذیرندگی و آمار</button>
  </nav>

  <div class="header-actions">
    <button class="icon-btn" onclick="toggleDrawer()" title="فهرست اسلایدها">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
        <line x1="3" y1="6" x2="21" y2="6"/>
        <line x1="3" y1="12" x2="21" y2="12"/>
        <line x1="3" y1="18" x2="21" y2="18"/>
      </svg>
      <span>فهرست اسلایدها</span>
    </button>
    <button class="icon-btn" onclick="toggleFullScreen()" title="نمایش تمام‌صفحه (کلید F)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
        <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>
      </svg>
      <span>تمام‌صفحه</span>
    </button>
  </div>
</header>
```

=== ./data/slides.json ===

```json
=== END OF PROJECT ===
```
