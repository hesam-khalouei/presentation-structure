# Project Source Code (Part 1)

این فایل شامل کد پروژه است. هر فایل با `=== path ===` مشخص شده و کد داخل بلوک ```lang``` است. base64 فونت/تصویر حذف شده.

---

=== ./index2.html (ادامه 1) ===

```
<!doctype html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>
      پرزنتیشن جامع راهکارهای سازمانی و اعتباری اوانو | Ewano B2B Interactive
      Deck
    </title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap"
      rel="stylesheet" />
    <style>
      /* =========================================================================
       EWANO BRAND BOOK DESIGN SYSTEM & COLOR TOKENS (Pages 09-38)
       Primary: Persian Green (#00D4B4 - 80%)
       Accent: Persian Orange (#FF7722 - 10%)
       Neutral Dark: Outer Space (#444444 / #14181D - 5%)
       Neutral Light: Whiteout (#F9FBFC - 5%)
       Secondary Marketing: Supernova (#FFDB04), Royal Purple (#6F59A9),
                            Persian Rose (#F16273), Sky Blue (#0093DD)
       ========================================================================= */
      @font-face {
        font-family: 'IRANYekanX';
        src:
          local('IRANYekanXVF'),
          local('IRANYekanX'),
          local('IRANYekanX-UltraLight'),
          url('data:...(base64 حذف شد برای صرفه‌جویی توکن)...')
            format('woff');
        font-weight: 100 300;
        font-style: normal;
        font-display: swap;
      }
      @font-face {
        font-family: 'IRANYekanX';
        src:
          local('IRANYekanXVF'),
          local('IRANYekanX'),
          local('IRANYekanX-Regular'),
          local('IRANYekanX-Medium'),
          url('data:...(base64 حذف شد برای صرفه‌جویی توکن)...')
            format('woff');
        font-weight: 400 500;
        font-style: normal;
        font-display: swap;
      }
      @font-face {
        font-family: 'IRANYekanX';
        src:
          local('IRANYekanXVF'),
          local('IRANYekanX'),
          local('IRANYekanX-Bold'),
          local('IRANYekanX-DemiBold'),
          local('IRANYekanX-ExtraBold'),
          local('IRANYekanX-Black'),
          url('data:...(base64 حذف شد برای صرفه‌جویی توکن)...')
            format('woff');
        font-weight: 600 900;
        font-style: normal;
        font-display: swap;
      }

      :root {
        --persian-green: #00d4b4;
        --persian-green-dark: #00a68c;
        --persian-green-deep: #007a66;
        --persian-green-glow: rgba(0, 212, 180, 0.28);
        --persian-green-soft: rgba(0, 212, 180, 0.12);
        --pastel-green: #3dd598;

        --persian-orange: #ff7722;
        --persian-orange-dark: #e05a00;
        --persian-orange-glow: rgba(255, 119, 34, 0.28);
        --persian-orange-soft: rgba(255, 119, 34, 0.12);

        --persian-rose: #f16273;
        --persian-rose-dark: #e0001a;
        --persian-rose-glow: rgba(255, 34, 60, 0.28);
        --persian-rose-soft: rgba(255, 34, 60, 0.12);

        --supernova: #ffdb04;
        --royal-purple: #6f59a9;
        
        --sky-blue: #0093dd;

        --outer-space: #444444;
        --bg-dark: #0e1318;
        --bg-dark-card: #171f26;
        --bg-dark-elevated: #1f2933;
        --whiteout: #f9fbfc;
        --text-light: #f9fbfc;
        --text-muted: #94a3b8;
        --border-glass: rgba(255, 255, 255, 0.1);
        --border-green: rgba(0, 212, 180, 0.35);

        --font-main:
          'IRANYekanX', 'Vazirmatn', -apple-system, BlinkMacSystemFont,
          'Segoe UI', Roboto, sans-serif;
      }

      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        user-select: none;
        -webkit-font-smoothing: antialiased;
      }

      html,
      body {
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        background-color: var(--bg-dark);
        color: var(--text-light);
        font-family: var(--font-main);
        direction: rtl;
      }

      /* AMBIENT ANIMATED BACKGROUND (Inspired by Brand Book Elemental Patterns & Figma Hero) */
      .ambient-canvas {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        overflow: hidden;
        background:
          radial-gradient(
            circle at 15% 18%,
            rgba(0, 212, 180, 0.13) 0%,
            transparent 42%
          ),
          radial-gradient(
            circle at 85% 82%,
            rgba(255, 119, 34, 0.09) 0%,
            transparent 42%
          ),
          radial-gradient(
            circle at 50% 50%,
            rgba(111, 89, 169, 0.06) 0%,
            transparent 60%
          ),
          linear-gradient(135deg, #0b0f13 0%, #121820 50%, #0d1318 100%);
      }

      .ambient-grid {
        position: absolute;
        inset: 0;
        background-image:
          linear-gradient(
            to right,
            rgba(255, 255, 255, 0.025) 1px,
            transparent 1px
          ),
          linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0.025) 1px,
            transparent 1px
          );
        background-size: 48px 48px;
        mask-image: radial-gradient(
          circle at center,
          black 40%,
          transparent 90%
        );
      }

      .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(85px);
        opacity: 0.45;
        animation: floatOrb 18s ease-in-out infinite alternate;
      }
      .orb-1 {
        width: 460px;
        height: 460px;
        background: var(--persian-green);
        top: -140px;
        right: -100px;
      }
      .orb-2 {
        width: 380px;
        height: 380px;
        background: var(--persian-orange);
        bottom: -140px;
        left: -80px;
        animation-delay: -6s;
      }
      .orb-3 {
        width: 300px;
        height: 300px;
        background: var(--sky-blue);
        top: 40%;
        left: 35%;
        opacity: 0.18;
        animation-delay: -11s;
      }

      @keyframes floatOrb {
        0% {
          transform: translate(0, 0) scale(1);
        }
        50% {
          transform: translate(-40px, 30px) scale(1.08);
        }
        100% {
          transform: translate(30px, -25px) scale(0.95);
        }
      }

      /* =========================================================================
       TOP HEADER BAR (Persistent Presentation Chrome)
       ========================================================================= */
      .deck-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 68px;
        padding: 0 36px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        z-index: 100;
        background: rgba(14, 19, 24, 0.78);
        backdrop-filter: blur(16px);
        border-bottom: 1px solid var(--border-glass);
      }

      .brand-cluster {
        display: flex;
        align-items: center;
        gap: 16px;
      }

      .logo-mark {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(
          135deg,
          var(--persian-green),
          var(--persian-green-dark)
        );
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 6px 18px var(--persian-green-glow);
        cursor: pointer;
        transition: transform 0.25s ease;
      }
      .logo-mark:hover {
        transform: scale(1.06) rotate(-4deg);
      }

      .brand-titles {
        display: flex;
        flex-direction: column;
      }
      .brand-titles .main-title {
        font-size: 16px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: -0.2px;
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .brand-titles .sub-title {
        font-size: 11px;
        color: var(--persian-green);
        font-weight: 700;
      }

      .co-pill {
        display: flex;
        align-items: center;
        gap: 10px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid var(--border-glass);
        padding: 5px 14px;
        border-radius: 999px;
        font-size: 11.5px;
        color: #cbd5e1;
        font-weight: 600;
      }
      .co-pill span.dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: var(--persian-green);
        box-shadow: 0 0 8px var(--persian-green);
      }

      /* Chapter Pills in Top Bar */
      .chapter-nav {
        display: flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.04);
        padding: 4px;
        border-radius: 12px;
        border: 1px solid var(--border-glass);
      }
      .chapter-btn {
        background: transparent;
        border: none;
        color: var(--text-muted);
        font-family: var(--font-main);
        font-size: 11.5px;
        font-weight: 700;
        padding: 6px 12px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.25s ease;
        white-space: nowrap;
      }
      .chapter-btn:hover {
        color: #ffffff;
        background: rgba(255, 255, 255, 0.06);
      }
      .chapter-btn.active {
        background: var(--persian-green);
        color: #0b0f13;
        font-weight: 900;
        box-shadow: 0 4px 12px var(--persian-green-glow);
      }

      .header-actions {
        display: flex;
        align-items: center;
        gap: 10px;
      }

      .icon-btn {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid var(--border-glass);
        color: #ffffff;
        height: 38px;
        padding: 0 14px;
        border-radius: 10px;
        display: inline-flex;
        align-items: center;
        gap: 7px;
        font-family: var(--font-main);
        font-size: 12px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      .icon-btn:hover {
        border-color: var(--persian-green);
        background: var(--persian-green-soft);
        color: var(--persian-green);
      }

      /* =========================================================================
       SLIDE STAGE & TRANSITIONS
       ========================================================================= */
      .stage-container {
        position: fixed;
        top: 68px;
        bottom: 64px;
        left: 0;
        right: 0;
        z-index: 10;
        overflow: hidden;
      }

      .slide {
        position: absolute;
        inset: 0;
        padding: 28px 56px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        opacity: 0;
        visibility: hidden;
        transform: translateY(28px) scale(0.985);
        transition:
          opacity 0.55s cubic-bezier(0.16, 1, 0.3, 1),
          transform 0.55s cubic-bezier(0.16, 1, 0.3, 1),
          visibility 0.55s;
        pointer-events: none;
        overflow-y: auto;
      }

      .slide.active {
        opacity: 1;
        visibility: visible;
        transform: translateY(0) scale(1);
        pointer-events: auto;
        z-index: 20;
      }

      .slide-inner {
        width: 100%;
        max-width: 1440px;
        margin: 0 auto;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 20px;
      }

      /* Staggered Entrance Animations inside active slide */
      .slide.active .anim-up {
        animation: fadeUpIn 0.65s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }
      .slide.active .delay-1 {
        animation-delay: 0.08s;
      }
      .slide.active .delay-2 {
        animation-delay: 0.16s;
      }
      .slide.active .delay-3 {
        animation-delay: 0.24s;
      }
      .slide.active .delay-4 {
        animation-delay: 0.32s;
      }
      .slide.active .delay-5 {
        animation-delay: 0.4s;
      }

      .anim-up {
        opacity: 0;
        transform: translateY(22px);
      }

      @keyframes fadeUpIn {
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }

      /* =========================================================================
       COMMON TYPOGRAPHY & VESSEL HEADERS (Ewano Brand Book p. 38)
       ========================================================================= */
      .slide-top-meta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        flex-wrap: wrap;
      }

      .eyebrow-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 5px 14px;
        border-radius: 999px;
        background: var(--persian-green-soft);
        border: 1px solid var(--border-green);
        color: var(--persian-green);
        font-size: 12px;
        font-weight: 800;
      }
      .eyebrow-badge.orange {
        background: var(--persian-orange-soft);
        border-color: rgba(255, 119, 34, 0.4);
        color: var(--persian-orange);
      }

      .slide-headline {
        font-size: clamp(24px, 2.5vw, 36px);
        font-weight: 900;
        color: #ffffff;
        line-height: 1.3;
        letter-spacing: -0.3px;
      }

      .header-wrapper {
        padding-bottom: 32px;
      }

      .slide-headline .accent-green {
        color: var(--persian-green);
      }
      .slide-headline .accent-orange {
        color: var(--persian-orange);
      }

      .slide-subtitle {
        font-size: clamp(13.5px, 1.1vw, 16px);
        color: #ffffff;
        line-height: 1.75;
        max-width: 960px;
      }

      .slide-subtitlee {
        font-size: clamp(13.5px, 1.1vw, 16px);
        color: #ffffff;
        line-height: 1.75;
      }

      /* Brand Book p.38 Cinematic Vessel Frame */
      .vessel-pill {
        display: inline-flex;
        align-items: center;
        border: 1.5px solid var(--persian-green);
        border-radius: 999px;
        padding: 2px 16px;
        color: var(--persian-green);
        font-weight: 800;
        font-size: 0.85em;
        margin: 0 6px;
        box-shadow: 0 0 18px rgba(0, 212, 180, 0.2);
      }

      /* =========================================================================
       CARDS, GRIDS & CONTAINERS
       ========================================================================= */
      .grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        align-items: center;
      }
      .grid-2-asym {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 28px;
        align-items: center;
      }
      .grid-3 {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
      }
      .grid-4 {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
      }
      .grid-5 {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 14px;
      }

      .glass-card {
        background: linear-gradient(
          145deg,
          rgba(25, 34, 43, 0.88) 0%,
          rgba(17, 24, 31, 0.92) 100%
        );
        border: 1px solid var(--border-glass);
        border-radius: 22px;
        padding: 22px 24px;
        position: relative;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 14px 34px rgba(0, 0, 0, 0.28);
      }
      .glass-card:hover {
        transform: translateY(-5px);
        border-color: var(--border-green);
        box-shadow: 0 18px 42px rgba(0, 212, 180, 0.14);
      }
      .glass-card.orange-hover:hover {
        border-color: rgba(255, 119, 34, 0.5);
        box-shadow: 0 18px 42px rgba(255, 119, 34, 0.15);
      }

      /* =========================================================================
       FIGMA LANDING INSPIRED 3D FLOATING WALLET CARDS (Hero & Slide 8)
       ========================================================================= */
      .hero-cards-stage {
        position: relative;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        perspective: 1200px;
      }

      .ewano-3d-card {
        width: 310px;
        height: 190px;
        border-radius: 22px;
        padding: 22px;
        color: #ffffff;
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 24px 50px rgba(0, 0, 0, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.25);
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        cursor: pointer;
        overflow: hidden;
      }
      .ewano-3d-card::after {
        content: 'EWANO';
        position: absolute;
        bottom: -18px;
        left: -10px;
        font-size: 68px;
        font-weight: 900;
        letter-spacing: 4px;
        color: rgba(255, 255, 255, 0.08);
        pointer-events: none;
        font-family: sans-serif;
      }

      .ewano-3d-card.card-welfare {
        background: linear-gradient(135deg, #00d4b4 0%, #008872 100%);
        transform: translate3d(-90px, -45px, 40px) rotate(-8deg);
        z-index: 3;
        animation: floatCard1 5s ease-in-out infinite alternate;
      }
      .ewano-3d-card.card-credit {
        background: linear-gradient(135deg, #ff7722 0%, #c84b00 100%);
        transform: translate3d(10px, 15px, 60px) rotate(4deg);
        z-index: 4;
        animation: floatCard2 5.5s ease-in-out infinite alternate;
      }
      .ewano-3d-card.card-cash {
        background: linear-gradient(135deg, #0093dd 0%, #00548a 100%);
        transform: translate3d(105px, 75px, 20px) rotate(14deg);
        z-index: 2;
        animation: floatCard3 6s ease-in-out infinite alternate;
      }

      .ewano-3d-card:hover {
        z-index: 10 !important;
        transform: translate3d(0, -10px, 90px) rotate(0deg) scale(1.06) !important;
        box-shadow: 0 30px 70px rgba(0, 212, 180, 0.4);
      }

      @keyframes floatCard1 {
        0% {
          transform: translate3d(-85px, -45px, 40px) rotate(-8deg);
        }
        100% {
          transform: translate3d(-95px, -58px, 50px) rotate(-5deg);
        }
      }
      @keyframes floatCard2 {
        0% {
          transform: translate3d(10px, 15px, 60px) rotate(3deg);
        }
        100% {
          transform: translate3d(15px, 2px, 75px) rotate(6deg);
        }
      }
      @keyframes floatCard3 {
        0% {
          transform: translate3d(100px, 75px, 20px) rotate(13deg);
        }
        100% {
          transform: translate3d(110px, 62px, 35px) rotate(10deg);
        }
      }

      .card-top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .card-chip {
        width: 38px;
        height: 28px;
        border-radius: 6px;
        background: linear-gradient(
          135deg,
          rgba(255, 255, 255, 0.45),
          rgba(255, 255, 255, 0.15)
        );
        border: 1px solid rgba(255, 255, 255, 0.4);
      }
      .card-balance-title {
        font-size: 18px;
        font-weight: 900;
        margin-top: 12px;
      }
      .card-balance-sub {
        font-size: 12px;
        opacity: 0.9;
      }

      /* =========================================================================
       ORBITAL ECOSYSTEM DIAGRAM (Slide 2 - MCI 12 Companies + 7 Services)
       ========================================================================= */
      .ecosystem-layout {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 24px;
        align-items: stretch;
      }
      .companies-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
      }
      .company-pill {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid var(--border-glass);
        border-radius: 14px;
        padding: 12px 14px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 13px;
        font-weight: 700;
        color: #e2e8f0;
        transition: all 0.25s ease;
      }
      .company-pill:hover {
        border-color: var(--persian-green);
        background: var(--persian-green-soft);
        transform: translateX(-4px);
      }
      .company-pill.featured-ebcom {
        background: linear-gradient(
          135deg,
          rgba(0, 212, 180, 0.22),
          rgba(0, 212, 180, 0.06)
        );
        border: 1.5px solid var(--persian-green);
        color: #ffffff;
        font-weight: 900;
        box-shadow: 0 8px 24px rgba(0, 212, 180, 0.2);
      }

      /* =========================================================================
       SUPER APP PHONE MOCKUP & 10 SERVICES (Slide 4 & Slide 8)
       ========================================================================= */
      .services-10-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
      }
      .service-tile {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid var(--border-glass);
        border-radius: 18px;
        padding: 16px 12px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        cursor: pointer;
        transition: all 0.28s ease;
      }
      .service-tile:hover,
      .service-tile.active {
        background: linear-gradient(
          180deg,
          rgba(0, 212, 180, 0.18) 0%,
          rgba(0, 212, 180, 0.04) 100%
        );
        border-color: var(--persian-green);
        transform: translateY(-5px);
        box-shadow: 0 12px 26px rgba(0, 212, 180, 0.18);
      }
      .service-icon-box {
        width: 52px;
        height: 52px;
        border-radius: 16px;
        background: rgba(0, 212, 180, 0.12);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--persian-green);
        transition: all 0.25s ease;
      }
      .service-tile:hover .service-icon-box,
      .service-tile.active .service-icon-box {
        background: var(--persian-green);
        color: #0b0f13;
        transform: scale(1.08);
      }
      .service-tile h4 {
        font-size: 13.5px;
        font-weight: 800;
        color: #ffffff;
      }
      .service-tile p {
        font-size: 11px;
        color: var(--text-muted);
        line-height: 1.45;
      }

      /* =========================================================================
       25 PARTNER BRANDS WALL (Slide 5)
       ========================================================================= */
      .brands-25-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
      }
      .brand-tile {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid var(--border-glass);
        border-radius: 16px;
        padding: 13px 14px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
      }
      .brand-tile::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        width: 4px;
        background: var(--brand-color, var(--persian-green));
      }
      .brand-tile:hover {
        transform: translateY(-4px) scale(1.02);
        background: rgba(255, 255, 255, 0.08);
        border-color: var(--brand-color, var(--persian-green));
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
      }
      .brand-tile-name {
        font-size: 13.5px;
        font-weight: 900;
        color: #ffffff;
      }
      .brand-tile-cat {
        font-size: 10.5px;
        color: var(--text-muted);
        background: rgba(255, 255, 255, 0.06);
        padding: 3px 8px;
        border-radius: 8px;
        font-weight: 700;
      }

      /* =========================================================================
       CREDIT JOURNEY STEPPER SLIDES (Slides 10 to 15 - 1 Step Per Slide!)
       ========================================================================= */
      .journey-progress-rail {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 10px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid var(--border-glass);
        padding: 12px 16px;
        border-radius: 18px;
      }
      .rail-step {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 12px;
        border-radius: 12px;
        cursor: pointer;
        opacity: 0.55;
        transition: all 0.25s ease;
        border: 1px solid transparent;
      }
      .rail-step:hover {
        opacity: 0.85;
        background: rgba(255, 255, 255, 0.04);
      }
      .rail-step.done {
        opacity: 0.85;
        color: var(--persian-green);
      }
      .rail-step.current {
        opacity: 1;
        background: linear-gradient(
          135deg,
          rgba(0, 212, 180, 0.2),
          rgba(0, 212, 180, 0.05)
        );
        border-color: var(--persian-green);
        box-shadow: 0 6px 20px rgba(0, 212, 180, 0.2);
      }
      .rail-num {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 13px;
        flex-shrink: 0;
      }
      .rail-step.current .rail-num {
        background: var(--persian-green);
        color: #0b0f13;
        box-shadow: 0 0 12px var(--persian-green);
      }
      .rail-step.done .rail-num {
        background: rgba(0, 212, 180, 0.25);
        color: var(--persian-green);
      }
      .rail-label {
        font-size: 12px;
        font-weight: 800;
        line-height: 1.3;
      }

      .step-hero-panel {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 28px;
        align-items: stretch;
      }

      .step-visual-box {
        background: radial-gradient(
          circle at center,
          rgba(0, 212, 180, 0.14) 0%,
          rgba(17, 24, 31, 0.95) 75%
        );
        border: 1px solid var(--border-green);
        border-radius: 24px;
        padding: 28px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
      }

      /* =========================================================================
       INTERACTIVE TABS & SEGMENTED CONTROLS
       ========================================================================= */
      .segmented-tabs {
        display: inline-flex;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid var(--border-glass);
        border-radius: 14px;
        padding: 5px;
        gap: 6px;
      }
      .seg-btn {
        background: transparent;
        border: none;
        color: var(--text-muted);
        font-family: var(--font-main);
        font-size: 13px;
        font-weight: 800;
        padding: 8px 18px;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.25s ease;
      }
      .seg-btn.active {
        background: var(--persian-green);
        color: #0b0f13;
        box-shadow: 0 4px 14px var(--persian-green-glow);
      }

      /* =========================================================================
       BOTTOM NAVIGATION BAR & PROGRESS
       ========================================================================= */
      .deck-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 64px;
        padding: 0 36px;
        background: rgba(14, 19, 24, 0.86);
        backdrop-filter: blur(16px);
        border-top: 1px solid var(--border-glass);
        display: flex;
        align-items: center;
        justify-content: space-between;
        z-index: 100;
      }

      .progress-track {
        position: absolute;
        top: -3px;
        left: 0;
        right: 0;
        height: 3px;
        background: rgba(255, 255, 255, 0.08);
      }
      .progress-fill {
        height: 100%;
        width: 5%;
        background: linear-gradient(
          90deg,
          var(--persian-orange),
          var(--persian-green)
        );
        box-shadow: 0 0 12px var(--persian-green);
        transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      }

      .nav-controls {
        display: flex;
        align-items: center;
        gap: 12px;
      }
      .nav-arrow-btn {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid var(--border-glass);
        color: #ffffff;
        height: 40px;
        padding: 0 18px;
        border-radius: 12px;
        font-family: var(--font-main);
        font-size: 13px;
        font-weight: 800;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      .nav-arrow-btn:hover:not(:disabled) {
        background: var(--persian-green);
        color: #0b0f13;
        border-color: var(--persian-green);
        box-shadow: 0 4px 16px var(--persian-green-glow);
      }
      .nav-arrow-btn:disabled {
        opacity: 0.35;
        cursor: not-allowed;
      }

      .slide-counter-pill {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid var(--border-glass);
        padding: 6px 16px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
        color: #e2e8f0;
        display: flex;
        align-items: center;
        gap: 8px;
      }

      .slide-dots {
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .slide-dot {
        width: 8px;
        height: 8px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.2);
        cursor: pointer;
        transition: all 0.3s ease;
      }
      .slide-dot:hover {
        background: rgba(0, 212, 180, 0.6);
      }
      .slide-dot.active {
        width: 26px;
        background: var(--persian-green);
        box-shadow: 0 0 10px var(--persian-green);
      }
      /* .slide-dot.journey-dot.active {
        background: var(--persian-orange);
        box-shadow: 0 0 10px var(--persian-orange);
      } */

      /* =========================================================================
       SLIDE DRAWER OVERLAY (Quick Jump Menu)
       ========================================================================= */
      .drawer-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.72);
        backdrop-filter: blur(8px);
        z-index: 200;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        display: flex;
        justify-content: flex-start;
      }
      .drawer-backdrop.open {
        opacity: 1;
        visibility: visible;
      }
      .drawer-panel {
        width: 420px;
        max-width: 90vw;
        height: 100%;
        background: #121820;
        border-left: 1px solid var(--border-glass);
        padding: 28px 24px;
        display: flex;
        flex-direction: column;
        gap: 18px;
        transform: translateX(100%);
        transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        overflow-y: auto;
      }
      .drawer-backdrop.open .drawer-panel {
        transform: translateX(0);
      }
      .drawer-item {
        padding: 12px 14px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid var(--border-glass);
        display: flex;
        align-items: center;
        gap: 12px;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      .drawer-item:hover,
      .drawer-item.active {
        border-color: var(--persian-green);
        background: var(--persian-green-soft);
      }
      .drawer-item-num {
        width: 28px;
        height: 28px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.08);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 12px;
        color: var(--persian-green);
        flex-shrink: 0;
      }
      .drawer-item.active .drawer-item-num {
        background: var(--persian-green);
        color: #0b0f13;
      }

      /* Pulse & SVG Motion Keyframes */
      @keyframes pulseRing {
        0% {
          transform: scale(0.92);
          opacity: 0.8;
        }
        50% {
          transform: scale(1.08);
          opacity: 0.35;
        }
        100% {
          transform: scale(0.92);
          opacity: 0.8;
        }
      }
      @keyframes dashFlow {
        to {
          stroke-dashoffset: -40;
        }
      }
      .svg-flow-line {
        stroke-dasharray: 6 6;
        animation: dashFlow 1.6s linear infinite;
      }
      .svg-pulse {
        transform-origin: center;
        animation: pulseRing 3s ease-in-out infinite;
      }

      /* Responsive adjustments for smaller projectors/laptops */
      @media (max-width: 1180px) {
        .chapter-nav {
          display: none;
        }
        .slide {
          padding: 20px 28px;
        }
        .grid-2,
        .grid-2-asym,
        .step-hero-panel,
        .ecosystem-layout {
          grid-template-columns: 1fr;
        }
        .services-10-grid,
        .brands-25-grid {
          grid-template-columns: repeat(3, 1fr);
        }
      }

      /* =========================================================================
       REQUIREMENT 1: GLOBAL IRANYEKANX ENFORCEMENT
       ========================================================================= */
      body,
      button,
      input,
      select,
      textarea,
      svg text,
      .phone-screen,
      .city-lbl,
      .city-n {
        font-family:
          'IRANYekanX',
          'Vazirmatn',
          -apple-system,
          BlinkMacSystemFont,
          sans-serif !important;
      }

      /* =========================================================================
       REQUIREMENT 2: EWANO CARD IMAGE ON SLIDE 1 CARDS
       ========================================================================= */
      .hero-cards-stage {
        position: relative;
        height: 430px;
        display: flex;
        align-items: center;
        justify-content: center;
        perspective: 1300px;
      }
      .ewano-3d-card {
        width: 340px;
        height: 205px;
        border-radius: 22px;
        padding: 20px 22px;
        padding-left: 118px;
        position: absolute;
      }
      .ewano-card-visual-thumb {
        position: absolute;
        left: 14px;
        top: 50%;
        transform: translateY(-50%) rotate(-5deg);
        width: 90px;
        height: 142px;
        border-radius: 11px;
        object-fit: cover;
        box-shadow:
          0 12px 26px rgba(0, 0, 0, 0.65),
          0 0 0 1.5px rgba(255, 255, 255, 0.32);
        transition:
          transform 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          box-shadow 0.45s ease;
        z-index: 4;
        pointer-events: none;
      }
      .ewano-3d-card:hover .ewano-card-visual-thumb {
        transform: translateY(-50%) rotate(0deg) scale(1.09);
        box-shadow:
          0 16px 34px rgba(0, 212, 180, 0.5),
          0 0 0 2px #ffffff;
      }
      .ewano-card-centerpiece {
        position: absolute;
        left: -30px;
        bottom: -18px;
        width: 145px;
        height: 228px;
        border-radius: 16px;
        object-fit: cover;
        box-shadow:
          0 24px 55px rgba(0, 0, 0, 0.8),
          0 0 0 2px rgba(0, 212, 180, 0.55);
        transform: rotate(-10deg);
        z-index: 6;
        transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
        cursor: pointer;
      }
      .ewano-card-centerpiece:hover {
        transform: rotate(0deg) scale(1.12) translateY(-8px);
        z-index: 15;
        box-shadow:
          0 30px 70px rgba(0, 212, 180, 0.55),
          0 0 0 2.5px #00d4b4;
      }

      /* =========================================================================
       REQUIREMENT 6: LARGER HEADINGS & ICONIC HOVER-TO-EXPAND BOXES
       ========================================================================= */
      .slide-headline {
        font-size: clamp(30px, 3.1vw, 46px) !important;
        font-weight: 900 !important;
        line-height: 1.28 !important;
        letter-spacing: -0.4px;
      }
      .glass-card h3 {
        font-size: clamp(20px, 1.7vw, 25px) !important;
        font-weight: 900 !important;
        line-height: 1.35 !important;
        transition:
          color 0.3s ease,
          transform 0.3s ease;
      }
      .glass-card h4,
      .service-tile h4 {
        font-size: clamp(16.5px, 1.35vw, 20px) !important;
        font-weight: 900 !important;
        line-height: 1.35 !important;
        transition: color 0.3s ease;
      }
      .brand-tile-name {
        font-size: 16px !important;
        font-weight: 900 !important;
      }

      /* Iconic First-Glance State & Smooth Hover-to-Expand */
      .glass-card:not(.no-collapse),
      .service-tile,
      .ewano-3d-card {
        transition: all 0.42s cubic-bezier(0.16, 1, 0.3, 1) !important;
      }

      .glass-card:not(.no-collapse) p,
      .glass-card:not(.no-collapse) ul,
      .glass-card:not(.no-collapse) .hover-reveal,
      .service-tile p,
      .ewano-3d-card .card-balance-sub {
        max-height: 0;
        opacity: 0;
        overflow: hidden;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        border-top-color: transparent !important;
        transform: translateY(8px);
        transition:
          max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          opacity 0.35s ease,
          transform 0.35s ease,
          margin 0.35s ease,
          padding 0.35s ease;
      }

      .glass-card:not(.no-collapse):hover,
      .glass-card:not(.no-collapse):focus-within {
        transform: translateY(-6px) scale(1.02) !important;
        border-color: var(--persian-green) !important;
        box-shadow: 0 22px 48px rgba(0, 212, 180, 0.2) !important;
        z-index: 12;
      }
      .glass-card.orange-hover:not(.no-collapse):hover {
        border-color: var(--persian-orange) !important;
        box-shadow: 0 22px 48px rgba(255, 119, 34, 0.22) !important;
      }

      .glass-card:not(.no-collapse):hover p,
      .glass-card:not(.no-collapse):hover ul,
      .glass-card:not(.no-collapse):hover .hover-reveal,
      .glass-card:not(.no-collapse):focus-within p,
      .glass-card:not(.no-collapse):focus-within ul,
      .glass-card:not(.no-collapse):focus-within .hover-reveal,
      .service-tile:hover p,
      .ewano-3d-card:hover .card-balance-sub {
        max-height: 360px;
        opacity: 1;
        transform: translateY(0);
        margin-top: 8px !important;
      }

      /* Make icons bigger in iconic collapsed mode */
      .service-icon-box {
        width: 60px !important;
        height: 60px !important;
        border-radius: 18px !important;
      }

      /* =========================================================================
       REQUIREMENT 3: CREDIT CALCULATOR STYLES (Adapted from ewano-b2b-deck.html)
       ========================================================================= */
      .calc-grid-layout {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 24px;
        align-items: stretch;
      }
      .calc {
        background: linear-gradient(
          145deg,
          rgba(25, 34, 43, 0.94) 0%,
          rgba(15, 21, 28, 0.98) 100%
        );
        border: 1px solid var(--border-green);
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }
      .calc-inputs {
        padding: 20px 26px;
        display: flex;
        flex-direction: column;
        gap: 16px;
      }
      .calc-row + .calc-row {
        padding-top: 14px;
        border-top: 1px solid var(--border-glass);
      }
      .calc-row-head {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 6px;
      }
      .calc-row-head label {
        font-size: 14px;
        font-weight: 800;
        color: #cbd5e1;
      }
      .calc-amount {
        font-size: 22px;
        font-weight: 900;
        color: var(--persian-green);
      }
      .calc-amount small {
        font-size: 12px;
        font-weight: 700;
        color: var(--text-muted);
        margin-right: 5px;
      }
      .calc-range {
        -webkit-appearance: none;
        appearance: none;
        width: 100%;
        height: 8px;
        border-radius: 999px;
        outline: none;
        cursor: pointer;
      }
      .calc-track {
        position: relative;
        height: 58px;
        --f: 0;
        direction: ltr;
      }
      .calc-track .calc-range {
        direction: ltr;
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        margin: 0;
        opacity: 0;
        z-index: 3;
        cursor: pointer;
      }
      .calc-line {
        position: absolute;
        top: 30px;
        left: 12px;
        right: 12px;
        height: 4px;
        margin-top: -2px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.14);
        overflow: hidden;
      }
      .calc-line i {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: calc(100% * var(--f));
        border-radius: 999px;
        background: linear-gradient(
          90deg,
          var(--persian-green),
          var(--persian-orange)
        );
      }
      .calc-ticks {
        position: absolute;
        top: 30px;
        left: 12px;
        right: 12px;
        height: 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        pointer-events: none;
      }
      .calc-ticks i {
        position: relative;
        width: 16px;
        height: 16px;
        margin: -8px;
        box-sizing: border-box;
        border-radius: 50%;
        background: #171f26;
        border: 2px solid rgba(255, 255, 255, 0.28);
        transition: all 0.22s ease;
        font-style: normal;
      }
      .calc-ticks i.on {
        border-color: var(--persian-green);
        background: rgba(0, 212, 180, 0.25);
      }
      .calc-ticks i.cur {
        background: var(--persian-green);
        border-color: #ffffff;
        transform: scale(1.28);
        box-shadow: 0 0 14px var(--persian-green);
      }
      .calc-ticks b {
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 11px;
        font-weight: 700;
        color: var(--text-muted);
        white-space: nowrap;
        direction: rtl;
      }
      .calc-ticks i.cur b {
        color: var(--persian-green);
        font-weight: 900;
        font-size: 12.5px;
      }
      .calc-pin {
        position: absolute;
        top: -2px;
        left: calc(12px + (100% - 24px) * var(--f));
        width: 24px;
        height: 28px;
        transform: translateX(-50%);
        pointer-events: none;
        transition: left 0.15s ease;
      }
      .calc-pin svg {
        width: 24px;
        height: 28px;
        display: block;
        color: var(--persian-orange);
        filter: drop-shadow(0 4px 10px rgba(255, 119, 34, 0.45));
      }
      .calc-result {
        position: relative;
        overflow: hidden;
        background: #090d11;
        color: #fafafa;
        padding: 20px 26px;
        border-top: 1px solid var(--border-glass);
        display: grid;
        grid-template-columns: 1fr 1.15fr;
        gap: 20px;
        align-items: center;
      }
      .calc-res-lbl {
        font-size: 13px;
        color: #94a3b8;
        font-weight: 800;
      }
      .calc-res-main {
        display: flex;
        align-items: baseline;
        gap: 8px;
        margin-top: 6px;
        flex-wrap: wrap;
      }
      .calc-res-main b {
        font-size: 32px;
        font-weight: 900;
        color: var(--persian-green);
        line-height: 1.15;
      }
      .calc-res-main span {
        font-size: 13px;
        color: #cbd5e1;
        font-weight: 700;
      }
      .calc-res-list {
        margin: 0;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px 18px;
        border-right: 1px solid rgba(255, 255, 255, 0.12);
        padding-right: 20px;
      }
      .calc-res-list div {
        display: flex;
        flex-direction: column;
        gap: 2px;
        font-size: 12px;
      }
      .calc-res-list dt {
        color: #94a3b8;
        font-weight: 700;
      }
      .calc-res-list dd {
        margin: 0;
        font-weight: 900;
        color: #ffffff;
        font-size: 13.5px;
      }

      /* =========================================================================
       REQUIREMENT 4: INTERACTIVE PHONE DEMO STYLES (From ewano-b2b-deck.html)
       ========================================================================= */
      .demo-slide-grid {
        display: grid;
        grid-template-columns: 0.95fr 1.05fr;
        gap: 28px;
        align-items: center;
      }
      .demo-wrap {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
      }
      .demo-clip {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
        justify-content: center;
      }
      .clip-btn {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        border: 1px solid var(--border-green);
        background: var(--bg-dark-elevated);
        color: var(--persian-green);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 14px rgba(0, 212, 180, 0.25);
      }
      .clip-btn svg {
        width: 15px;
        height: 15px;
      }
      .clip-steps {
        display: flex;
        gap: 5px;
        flex-wrap: wrap;
        justify-content: center;
      }
      .clip-steps span {
        font-size: 11px;
        font-weight: 800;
        padding: 4px 10px;
        border-radius: 999px;
        border: 1px solid var(--border-glass);
        color: #cbd5e1;
        background: rgba(255, 255, 255, 0.05);
        transition: all 0.25s;
        cursor: pointer;
      }
      .clip-steps span.on {
        color: #0b0f13;
        border-color: var(--persian-green);
        background: var(--persian-green);
        box-shadow: 0 0 12px var(--persian-green-glow);
      }
      .phone {
        width: 320px;
        height: 610px;
        background: #111113;
        border-radius: 40px;
        padding: 10px;
        box-shadow:
          0 24px 60px rgba(0, 0, 0, 0.65),
          0 0 0 2px rgba(0, 212, 180, 0.35);
        position: relative;
        flex-shrink: 0;
      }
      .phone-notch {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        width: 96px;
        height: 20px;
        background: #111113;
        border-radius: 0 0 14px 14px;
        z-index: 2;
      }
      .phone-screen {
        width: 100%;
        height: 100%;
        background: #ffffff;
        border-radius: 31px;
        overflow: hidden;
        position: relative;
        direction: rtl;
        color: #09090b;
        display: flex;
        flex-direction: column;
      }
      .ph-statusbar {
        height: 26px;
        padding: 8px 18px 0;
        display: flex;
        justify-content: space-between;
        font-size: 10px;
        font-weight: 700;
        color: #09090b;
        direction: ltr;
        flex-shrink: 0;
      }
      .ph-body {
        flex: 1;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
      }
      .phone * {
        scrollbar-width: none;
        -ms-overflow-style: none;
      }
      .phone *::-webkit-scrollbar {
        display: none;
        width: 0;
        height: 0;
      }
      .cc-dot,
      .cc-peek {
        cursor: pointer;
      }
      .ph-screen {
        display: none;
        flex: 1;
        flex-direction: column;
        overflow-y: auto;
      }
      .ph-screen.active {
        display: flex;
      }
      .ph-nav {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        height: 58px;
        padding: 7px 8px 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(8px);
        border-top: 1px solid #e4e4e7;
        flex-shrink: 0;
      }
      .ph-nav a {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2px;
        text-decoration: none;
        cursor: pointer;
      }
      .ph-nav .ic-wrap {
        width: 42px;
        height: 24px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .ph-nav .ic-wrap.on {
        background: #e8f8f6;
        box-shadow: inset 0 0 0 1px #00d4b4;
      }
      .ph-nav .ic-wrap.on svg {
        color: #00a68c !important;
      }
      .ph-nav .lbl {
        font-size: 9.5px;
        font-weight: 600;
        color: #71717a;
      }
      .ph-nav .lbl.on {
        font-weight: 800;
        color: #09090b;
      }
      .ph-finger {
        position: absolute;
        left: 0;
        top: 0;
        width: 34px;
        height: 34px;
        margin: -17px 0 0 -17px;
        border-radius: 50%;
        z-index: 60;
        pointer-events: none;
        opacity: 0;
        background: rgba(0, 212, 180, 0.28);
        box-shadow:
          0 0 0 2px rgba(255, 255, 255, 0.95),
          0 6px 14px rgba(0, 0, 0, 0.3);
        transition:
          transform 0.55s cubic-bezier(0.3, 0.8, 0.3, 1),
          opacity 0.3s;
      }
      .ph-finger.show {
        opacity: 1;
      }
      .ph-finger.tap::after {
        content: '';
        position: absolute;
        inset: -4px;
        border-radius: 50%;
        border: 2px solid #00d4b4;
        animation: ph-tap 0.45s ease-out forwards;
      }
      @keyframes ph-tap {
        from {
          transform: scale(0.6);
          opacity: 1;
        }
        to {
          transform: scale(1.8);
          opacity: 0;
        }
      }
      #ph-c2c,
      #ph-invest,
      #ph-store,
      #ph-search {
        position: relative;
        background: #f7f8fa;
      }
      .phx-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 14px;
        background: #fff;
        border-bottom: 1px solid #eef0f2;
      }
      .phx-head b {
        font-size: 13.5px;
        font-weight: 800;
        color: #09090b;
      }
      .phx-back,
      .phx-sp {
        width: 28px;
        height: 28px;
      }
      .phx-back {
        border-radius: 50%;
        background: #f4f4f5;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: #09090b;
      }
      .phx-back svg {
        width: 15px;
        height: 15px;
      }
      .phx-body {
        padding: 12px;
        display: flex;
        flex-direction: column;
        gap: 10px;
      }
      .phx-src {
        border-radius: 16px;
        padding: 12px 14px;
        color: #fff;
        background: linear-gradient(135deg, #27dcae 0%, #0aae97 100%);
        box-shadow: 0 10px 20px rgba(10, 174, 151, 0.28);
        display: flex;
        flex-direction: column;
        gap: 2px;
      }
      .phx-src-lbl {
        font-size: 10px;
        opacity: 0.85;
      }
      .phx-src b {
        font-size: 12.5px;
      }
      .phx-pan {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.05em;
        direction: ltr;
        text-align: right;
        margin-top: 4px;
      }
      .phx-bal {
        font-size: 10px;
        opacity: 0.9;
      }
      .phx-f {
        display: flex;
        flex-direction: column;
        gap: 5px;
      }
      .phx-f > span {
        font-size: 10.5px;
        font-weight: 700;
        color: #52525b;
      }
      .phx-f input {
        font: inherit;
        font-size: 14px;
        font-weight: 700;
        padding: 9px 11px;
        border-radius: 10px;
        border: 1px solid #e4e4e7;
        background: #fff;
        color: #09090b;
        outline: none;
        text-align: right;
      }
      .phx-owner {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 10.5px;
        color: #52525b;
        background: #eaf6fc;
        border-radius: 9px;
        padding: 7px 9px;
      }
      .phx-owner b {
        color: #09090b;
      }
      .phx-bank {
        font-size: 9px;
        font-weight: 800;
        color: #fff;
        background: #e5484d;
        border-radius: 5px;
        padding: 2px 5px;
      }
      .phx-quick {
        display: flex;
        gap: 5px;
      }
      .phx-quick button {
        flex: 1;
        font: inherit;
        font-size: 10px;
        font-weight: 700;
        padding: 6px 4px;
        border-radius: 8px;
        border: 1px solid #e4e4e7;
        background: #fff;
        cursor: pointer;
        color: #09090b;
      }
      .phx-btn {
        font: inherit;
        font-size: 12.5px;
        font-weight: 800;
        padding: 11px;
        border-radius: 12px;
        border: 0;
        background: #0088cc;
        color: #fff;
        cursor: pointer;
      }
      .phx-btn:disabled {
        opacity: 0.4;
        cursor: not-allowed;
      }
      .phx-btn.ghost {
        background: #f4f4f5;
        color: #09090b;
      }
      .phx-sheet[hidden],
      .phx-sheet-in[hidden],
      .phx-rcpt[hidden] {
        display: none !important;
      }
      .phx-pop {
        align-items: center !important;
        justify-content: center;
        padding: 16px;
      }
      .phx-pop .phx-sheet-in {
        border-radius: 18px;
        box-shadow: 0 20px 44px rgba(9, 9, 11, 0.4);
      }
      .phx-rcpt {
        position: absolute;
        inset: 0;
        z-index: 6;
        background: #f7f8fa;
        display: flex;
        flex-direction: column;
        padding: 14px;
        gap: 10px;
        overflow-y: auto;
      }
      .rc-top {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
        text-align: center;
        padding: 10px 0 4px;
      }
      .rc-top b {
        font-size: 13px;
        font-weight: 800;
      }
      .rc-amt {
        font-size: 20px;
        font-weight: 900;
        color: #0088cc;
      }
      .rc-amt small {
        font-size: 10.5px;
        color: #71717a;
        font-weight: 600;
      }
      .rc-card {
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 14px;
        padding: 6px 12px;
        position: relative;
      }
      .rc-ok {
        color: #0b8043 !important;
      }
      .rc-acts {
        display: flex;
        gap: 8px;
        margin-top: auto;
      }
      .rc-acts .phx-btn {
        flex: 1;
        font-size: 11.5px;
        padding: 10px 6px;
      }
      .phx-sheet {
        position: absolute;
        inset: 0;
        z-index: 5;
        background: rgba(9, 9, 11, 0.45);
        display: flex;
        align-items: flex-end;
      }
      .phx-sheet-in {
        width: 100%;
        background: #fff;
        border-radius: 20px 20px 0 0;
        padding: 16px;
        display: flex;
        flex-direction: column;
        gap: 9px;
      }
      .phx-sheet-t {
        font-size: 13.5px;
        font-weight: 800;
        text-align: center;
      }
      .phx-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 11px;
        color: #52525b;
        padding: 5px 0;
        border-bottom: 1px solid #f4f4f5;
      }
      .phx-row b {
        color: #09090b;
        font-size: 11.5px;
      }
      .phx-done {
        align-items: center;
        text-align: center;
      }
      .phx-ok {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: #e8f8f6;
        color: #00a98e;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 0 1px #00c8a8 inset;
      }
      .phx-ok svg {
        width: 26px;
        height: 26px;
      }
      .phx-done-amt {
        font-size: 16px;
        font-weight: 900;
        color: #0088cc;
      }
      .phx-muted {
        font-size: 10px;
        color: #71717a;
      }
      .phx-bal2 {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 10.5px;
        color: #52525b;
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 11px;
        padding: 9px 11px;
      }
      .phx-bal2 b {
        font-size: 11.5px;
        color: #09090b;
      }
      .inv-list {
        display: flex;
        flex-direction: column;
        gap: 7px;
      }
      .inv-item {
        font: inherit;
        display: flex;
        align-items: center;
        gap: 9px;
        padding: 9px 11px;
        border-radius: 12px;
        background: #fff;
        border: 1px solid #eef0f2;
        cursor: pointer;
        text-align: right;
        color: #09090b;
      }
      .inv-item.on {
        border-color: #0088cc;
        box-shadow: 0 0 0 2px rgba(0, 136, 204, 0.15);
      }
      .inv-ic {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 9px;
        font-weight: 900;
        color: #fff;
        flex-shrink: 0;
      }
      .inv-name {
        flex: 1;
        display: flex;
        flex-direction: column;
      }
      .inv-name b,
      .inv-price b {
        font-size: 11.5px;
      }
      .inv-name small,
      .inv-price small {
        font-size: 9px;
        color: #71717a;
      }
      .inv-price {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
      }
      .up {
        color: #12a48c !important;
        font-weight: 700;
      }
      .inv-detail {
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 14px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      .inv-d-head {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
      }
      .inv-d-head b {
        font-size: 12px;
      }
      .inv-d-price {
        display: flex;
        align-items: baseline;
        gap: 6px;
      }
      .inv-d-price b {
        font-size: 17px;
        font-weight: 900;
      }
      .inv-spark {
        width: 100%;
        height: 40px;
        display: block;
      }
      .inv-spark path {
        fill: none;
        stroke: #12a48c;
        stroke-width: 2.2;
        vector-effect: non-scaling-stroke;
      }
      .inv-est {
        font-size: 10.5px;
        color: #0070a8;
        font-weight: 700;
        min-height: 1.2em;
      }
      .phx-note {
        font-size: 9px;
        color: #a1a1aa;
        text-align: center;
        margin: 0;
      }
      .ew-ic {
        width: 34px;
        height: 34px;
        border-radius: 10px;
        background: #e8f8f6;
        box-shadow: inset 0 0 0 1px #00c8a8;
        color: #00c8a8;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
      }
      .ew-ic svg {
        width: 18px;
        height: 18px;
        color: inherit;
      }
      .ew-ic.sm {
        width: 26px;
        height: 26px;
        border-radius: 8px;
      }
      .ew-ic.sm svg {
        width: 14px;
        height: 14px;
      }
      .st-body {
        flex: 1;
        overflow-y: auto;
      }
      .st-brand {
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 16px;
        padding: 12px;
      }
      .st-top {
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .st-logo {
        width: 46px;
        height: 46px;
        border-radius: 13px;
        background: #fff;
        border: 1px solid #e4e4e7;
        padding: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        flex-shrink: 0;
      }
      .st-logo img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
      }
      .st-id {
        flex: 1;
        display: flex;
        flex-direction: column;
        min-width: 0;
      }
      .st-id b {
        font-size: 13px;
      }
      .st-id span {
        font-size: 10px;
        color: #71717a;
      }
      .st-cb {
        font-size: 9px;
        font-weight: 800;
        color: #0b8043;
        background: #eaf6ee;
        border-radius: 99px;
        padding: 4px 8px;
        white-space: nowrap;
      }
      .st-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        margin-top: 10px;
      }
      .st-tags span {
        font-size: 9.5px;
        font-weight: 600;
        color: #52525b;
        background: #f4f4f5;
        border-radius: 99px;
        padding: 3px 9px;
      }
      .st-card {
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 14px;
        overflow: hidden;
      }
      .st-row {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 9px 11px;
        font-size: 10.5px;
      }
      .st-row + .st-row {
        border-top: 1px solid #f4f4f5;
      }
      .st-k {
        flex: 1;
        font-weight: 600;
      }
      .st-v {
        color: #71717a;
        font-size: 10px;
      }
      .st-green {
        color: #0b8043;
        font-weight: 700;
      }
      .st-h {
        font-size: 11.5px;
        font-weight: 800;
        margin: 2px 0 6px;
      }
      .st-about {
        margin: 0;
        font-size: 10px;
        line-height: 1.85;
        color: #52525b;
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 12px;
        padding: 9px 11px;
      }
      .st-search {
        display: flex;
        align-items: center;
        gap: 7px;
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 10px;
        padding: 8px 10px;
        margin-bottom: 7px;
        font-size: 10px;
        color: #a1a1aa;
      }
      .st-search svg {
        width: 14px;
        height: 14px;
        color: #a1a1aa;
      }
      .st-br {
        padding: 9px 11px;
      }
      .st-br + .st-br {
        border-top: 1px solid #f4f4f5;
      }
      .st-br-h {
        display: flex;
        justify-content: space-between;
        font-size: 11px;
        font-weight: 700;
      }
      .st-br-h span {
        font-size: 9px;
        color: #71717a;
        font-weight: 500;
      }
      .st-br p {
        margin: 3px 0 6px;
        font-size: 9.5px;
        color: #71717a;
        line-height: 1.6;
      }
      .st-br-acts {
        display: flex;
        gap: 5px;
      }
      .st-br-acts span {
        font-size: 9.5px;
        font-weight: 700;
        padding: 5px 9px;
        border-radius: 8px;
        background: #f4f4f5;
        color: #52525b;
      }
      .st-br-acts span.nav {
        background: #eaf6fc;
        color: #0088cc;
      }
      .st-actions {
        display: flex;
        gap: 7px;
        padding: 9px 12px 10px;
        background: #fff;
        border-top: 1px solid #eef0f2;
      }
      .st-actions .phx-btn {
        flex: 1;
        padding: 9px;
        font-size: 11.5px;
      }
      .sr-head {
        gap: 7px;
      }
      .sr-box {
        flex: 1;
        display: flex;
        align-items: center;
        gap: 7px;
        background: #f4f4f5;
        border-radius: 10px;
        padding: 7px 10px;
      }
      .sr-box svg {
        width: 15px;
        height: 15px;
        color: #a1a1aa;
        flex-shrink: 0;
      }
      .sr-box input {
        flex: 1;
        min-width: 0;
        border: 0;
        outline: 0;
        background: none;
        font: inherit;
        font-size: 11.5px;
        color: #09090b;
      }
      .sr-head .phx-sp {
        display: none;
      }
      .sr-chips {
        display: flex;
        gap: 5px;
      }
      .sr-chips span {
        font-size: 10px;
        font-weight: 700;
        padding: 5px 10px;
        border-radius: 99px;
        background: #fff;
        border: 1px solid #e4e4e7;
        color: #52525b;
      }
      .sr-chips span.on {
        background: #0088cc;
        border-color: #0088cc;
        color: #fff;
      }
      .sr-hist {
        display: flex;
        flex-direction: column;
      }
      .sr-hist span {
        font-size: 10.5px;
        padding: 9px 11px;
      }
      .sr-hist span + span {
        border-top: 1px solid #f4f4f5;
      }
      .sr-cats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 7px;
      }
      .sr-cat {
        background: #fff;
        border: 1px solid #eef0f2;
        border-radius: 12px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        gap: 5px;
      }
      .sr-cat b {
        font-size: 10.5px;
      }
      .sr-cat small {
        font-size: 9px;
        color: #71717a;
      }
      .sr-res {
        display: flex;
        align-items: center;
        gap: 9px;
        padding: 9px 11px;
        font-size: 11px;
        font-weight: 700;
        cursor: pointer;
      }
      .sr-res + .sr-res {
        border-top: 1px solid #f4f4f5;
      }
      .sr-res img {
        width: 28px;
        height: 28px;
        object-fit: contain;
        border-radius: 50%;
        border: 1px solid #e4e4e7;
        padding: 3px;
        background: #fff;
      }
      .sr-res small {
        display: block;
        font-size: 9px;
        color: #71717a;
        font-weight: 500;
      }
      .qr-line {
        position: absolute;
        right: 6px;
        left: 6px;
        top: 8%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #38b6f0, transparent);
        animation: qr-line 1.8s ease-in-out infinite alternate;
      }
      @keyframes qr-line {
        to {
          top: 92%;
        }
      }
      .qr-sim {
        position: absolute;
        left: 50%;
        bottom: 82px;
        transform: translateX(-50%);
        font: inherit;
        font-size: 10px;
        font-weight: 700;
        color: #fff;
        background: rgba(56, 182, 240, 0.22);
        border: 1px solid rgba(56, 182, 240, 0.55);
        border-radius: 99px;
        padding: 5px 12px;
        cursor: pointer;
      }
      #qrSheet {
        color: #09090b;
      }
      .qr-merch {
        display: flex;
        align-items: center;
        gap: 9px;
      }
      .qr-merch b {
        display: block;
        font-size: 12.5px;
      }
      .qr-merch div {
        display: flex;
        flex-direction: column;
      }
      .qr-wallets {
        display: flex;
        gap: 5px;
      }
      .qr-wallets button {
        flex: 1;
        font: inherit;
        font-size: 10.5px;
        font-weight: 700;
        padding: 7px;
        border-radius: 9px;
        border: 1px solid #e4e4e7;
        background: #fff;
        color: #09090b;
        cursor: pointer;
      }
      .qr-wallets button.on {
        border-color: #00c8a8;
        background: #e8f8f6;
        color: #0a8a74;
      }
      .qr-rcpt {
        align-self: stretch;
        text-align: right;
      }
      .chat-typing {
        display: inline-flex;
        gap: 3px;
      }
      .chat-typing i {
        width: 5px;
        height: 5px;
        border-radius: 50%;
        background: #a1a1aa;
        animation: chat-dot 1s infinite;
      }
      .chat-typing i:nth-child(2) {
        animation-delay: 0.15s;
      }
      .chat-typing i:nth-child(3) {
        animation-delay: 0.3s;
      }
      @keyframes chat-dot {
        50% {
          opacity: 0.3;
          transform: translateY(-2px);
        }
      }
      .demo-tabs {
        display: flex;
        gap: 4px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid var(--border-glass);
        padding: 4px;
        border-radius: 12px;
        flex-wrap: wrap;
        justify-content: center;
      }
      .demo-tab {
        padding: 6px 14px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: 800;
        cursor: pointer;
        color: #cbd5e1;
        border: none;
        background: none;
        font-family: inherit;
        transition: 0.2s;
      }
      .demo-tab.active {
        background: var(--persian-green);
        color: #0b0f13;
        box-shadow: 0 4px 12px var(--persian-green-glow);
      }

      /* =========================================================================
       REQUIREMENT 5: IRAN MAP INFOGRAPHIC STYLES (From ewano-b2b-deck.html)
       ========================================================================= */
      .network-map-grid {
        display: grid;
        grid-template-columns: 1.05fr 0.95fr;
        gap: 22px;
        align-items: center;
      }
      .imap {
        margin-bottom: 0;
      }
      .imap-map {
        background: rgba(17, 24, 31, 0.85);
        border: 1px solid var(--border-green);
        border-radius: 22px;
        padding: 14px 18px;
        position: relative;
        box-shadow: 0 16px 38px rgba(0, 0, 0, 0.35);
      }
      .imap-svg {
        width: 100%;
        max-width: 470px;
        max-height: 340px;
        height: auto;
        display: block;
        margin: 0 auto;
        direction: ltr;
        overflow: visible;
      }
      .imap-prov {
        stroke: #0e1318;
        stroke-width: 1.5;
        stroke-linejoin: round;
        cursor: pointer;
        outline: none;
        transition:
          fill 0.25s,
          opacity 0.25s,
          filter 0.25s,
          transform 0.25s;
      }
      .imap-prov.t4 {
        fill: #00d4b4;
      }
      .imap-prov.t3 {
        fill: #0093dd;
      }
      .imap-prov.t2 {
        fill: #38bdf8;
      }
      .imap-prov.t1 {
        fill: #334155;
      }
      .imap-prov.t0 {
        fill: #1e293b;
      }
      .imap-prov:hover,
      .imap-prov:focus-visible {
        filter: brightness(1.22) drop-shadow(0 4px 12px rgba(0, 212, 180, 0.45));
        stroke: #ffffff;
        stroke-width: 2.2;
      }
      .imap-tip {
        position: absolute;
        z-index: 30;
        pointer-events: none;
        background: #0b0f13;
        border: 1.5px solid var(--persian-green);
        border-radius: 10px;
        box-shadow: 0 10px 26px rgba(0, 0, 0, 0.65);
        padding: 7px 13px;
        font-size: 12.5px;
        font-weight: 900;
        color: #ffffff;
        opacity: 0;
        transform: translate(-50%, calc(-100% - 10px));
        transition: opacity 0.18s ease;
        white-space: nowrap;
      }
      .imap-tip.show {
        opacity: 1;
      }
      .imap-tip small {
        color: var(--persian-green);
        font-weight: 800;
        margin-right: 8px;
      }
      .imap-legend {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px 16px;
        margin-top: 8px;
        font-size: 11.5px;
        color: #cbd5e1;
        font-weight: 700;
      }
      .imap-legend span {
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }
      .imap-legend i {
        width: 12px;
        height: 12px;
        border-radius: 3px;
        display: inline-block;
      }
      .imap-legend .t4 {
        background: #00d4b4;
      }
      .imap-legend .t3 {
        background: #0093dd;
      }
      .imap-legend .t2 {
        background: #38bdf8;
      }
      .imap-legend .t1 {
        background: #334155;
      }
      .logo-dots {
        --dot: 62px;
        --gap: 12px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: var(--gap);
        margin: 4px auto 0;
      }
      .logo-dot {
        width: var(--dot);
        height: var(--dot);
        border-radius: 50%;
        background: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        transition: transform 0.25s ease;
      }
      .logo-dot:hover {
        transform: translateY(-4px) scale(1.12);
        box-shadow: 0 10px 24px rgba(0, 212, 180, 0.4);
      }
      .logo-dot img {
        max-width: 76%;
        max-height: 56%;
        object-fit: contain;
        display: block;
      }
      .logo-dots.lm {
        display: block;
        overflow: hidden;
        padding-block: 10px;
        margin-block: -10px;
        -webkit-mask-image: linear-gradient(
          90deg,
          transparent,
          #000 7%,
          #000 93%,
          transparent
        );
        mask-image: linear-gradient(
          90deg,
          transparent,
          #000 7%,
          #000 93%,
          transparent
        );
      }
      .lm-track {
        display: flex;
        width: max-content;
        animation: lm-slide var(--lm-dur, 45s) linear infinite;
      }
      .lm-set {
        display: flex;
        gap: var(--gap);
        padding-inline-end: var(--gap);
      }
      .logo-dots.lm:hover .lm-track {
        animation-play-state: paused;
      }
      @keyframes lm-slide {
        from {
          transform: translateX(0);
        }
        to {
          transform: translateX(50%);
        }
      }

      /* =========================================================================
       REFINED 4-CARD STAGE ON SLIDE 1 (Blue, Orange, Green + 4th Black Debit Card)
       ========================================================================= */
      .hero-cards-stage {
        position: relative;
        height: 440px;
        display: flex;
        align-items: center;
        justify-content: center;
        perspective: 1400px;
      }
      .ewano-3d-card {
        width: 325px;
        height: 196px;
        border-radius: 22px;
        padding: 20px 22px;
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 22px 46px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.25);
        transition:
          transform 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          box-shadow 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          border-color 0.35s ease !important;
        cursor: default;
        overflow: hidden;
        transform-origin: top center;
      }
      .ewano-3d-card .card-balance-sub {
        max-height: 60px !important;
        opacity: 0.92 !important;
        transform: none !important;
        margin-top: 4px !important;
        font-size: 12px;
        line-height: 1.45;
      }

      /* Card 1: Welfare (Blue) */
      .ewano-3d-card.card-welfare {
        background: linear-gradient(135deg, #0093dd 0%, #00548a 100%);
        transform: translate3d(-115px, -105px, 10px) rotate(-9deg);
        z-index: 2;
        animation: none !important;
      }
      /* Card 2: Credit (Orange) */
      .ewano-3d-card.card-credit {
        background: linear-gradient(135deg, #ff7722 0%, #c84b00 100%);
        transform: translate3d(-40px, -38px, 30px) rotate(-3deg);
        z-index: 3;
        animation: none !important;
      }
      /* Card 3: Cash (Green) */
      .ewano-3d-card.card-cash {
        background: linear-gradient(135deg, #00d4b4 0%, #008872 100%);
        transform: translate3d(35px, 30px, 50px) rotate(3deg);
        z-index: 4;
        animation: none !important;
      }
      /* Card 4: Black Ewano Bank Debit Card (مشکی) */
      .ewano-3d-card.card-debit-black {
        background: linear-gradient(
          135deg,
          #2a2d32 0%,
          #121417 55%,
          #090a0c 100%
        );
        border: 1.5px solid rgba(255, 255, 255, 0.32);
        transform: translate3d(110px, 98px, 70px) rotate(9deg);
        z-index: 5;
        padding: 0;
        animation: none !important;
      }
      .ewano-3d-card.card-debit-black::after {
        display: none;
      }
      .debit-card-bg-img {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center 42%;
        opacity: 0.42;
        mix-blend-mode: luminosity;
        pointer-events: none;
        transition:
          opacity 0.4s ease,
          transform 0.5s ease;
      }
      .debit-card-overlay {
        position: relative;
        z-index: 2;
        width: 100%;
        height: 100%;
        padding: 20px 22px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: linear-gradient(
          135deg,
          rgba(15, 18, 22, 0.45) 0%,
          rgba(10, 12, 15, 0.82) 100%
        );
      }

      /* Smooth individual card hover in place without jumping to center */
      .ewano-3d-card.card-welfare:hover {
        z-index: 20 !important;
        transform: translate3d(-115px, -118px, 110px) rotate(0deg) scale(1.06) !important;
        box-shadow: 0 30px 65px rgba(0, 147, 221, 0.5) !important;
        border-color: #ffffff !important;
      }
      .ewano-3d-card.card-credit:hover {
        z-index: 20 !important;
        transform: translate3d(-40px, -52px, 110px) rotate(0deg) scale(1.06) !important;
        box-shadow: 0 30px 65px rgba(255, 119, 34, 0.5) !important;
        border-color: #ffffff !important;
      }
      .ewano-3d-card.card-cash:hover {
        z-index: 20 !important;
        transform: translate3d(35px, 16px, 110px) rotate(0deg) scale(1.06) !important;
        box-shadow: 0 30px 65px rgba(0, 212, 180, 0.5) !important;
        border-color: #ffffff !important;
      }
      .ewano-3d-card.card-debit-black:hover {
        z-index: 20 !important;
        transform: translate3d(110px, 84px, 110px) rotate(0deg) scale(1.06) !important;
        box-shadow:
          0 30px 70px rgba(0, 0, 0, 0.9),
          0 0 28px rgba(0, 212, 180, 0.45) !important;
        border-color: var(--persian-green) !important;
      }
      .ewano-3d-card.card-debit-black:hover .debit-card-bg-img {
        opacity: 0.62;
        transform: scale(1.05);
      }

      /* =========================================================================
       DOWNWARD-ONLY BOX EXPANSION ON HOVER & SIBLING STABILITY
       ========================================================================= */
      /* Keep grid items anchored at the top so expanding one item downward never stretches or moves siblings */
      .grid-2,
      .grid-3,
      .grid-4,
      .grid-5,
      .services-10-grid {
        align-items: start !important;
      }
      /* Exceptions where explicit top-and-bottom alignment is required */
      .slide3-equal-grid,
      .slide7-aligned-grid,
      .calc-grid-layout {
        align-items: stretch !important;
      }
      .demo-slide-grid {
        align-items: end !important;
      }

      .glass-card:not(.no-collapse),
      .service-tile {
        transform-origin: top center !important;
        transition:
          border-color 0.3s ease,
          box-shadow 0.3s ease,
          background 0.3s ease !important;
      }

      /* Do NOT move box upward on hover; keep top edge fixed and expand downward */
      .glass-card:hover,
      .glass-card:not(.no-collapse):hover,
      .glass-card:not(.no-collapse):focus-within,
      .service-tile:hover {
        transform: none !important;
        border-color: var(--persian-green) !important;
        box-shadow: 0 20px 44px rgba(0, 212, 180, 0.18) !important;
        z-index: 15;
      }
      .glass-card.orange-hover:not(.no-collapse):hover {
        transform: none !important;
        border-color: var(--persian-orange) !important;
        box-shadow: 0 20px 44px rgba(255, 119, 34, 0.2) !important;
      }

      /* Remove "" completely */
      .glass-card::after,
      .glass-card:not(.no-collapse)::after {
        content: none !important;
        display: none !important;
      }

      /* Slide 3 Equal Size Boxes */
      .slide3-equal-card {
        min-height: 250px;
        height: 100%;
      }

      /* Slide 7 Top & Bottom Alignment */
      .slide7-aligned-grid {
        align-items: stretch !important;
      }
      .slide7-right-box {
        height: 100%;
      }
      .slide7-left-stack {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 14px;
      }

      /* Slide 8 Bottom Alignment between Phone Mockup and Left Boxes */
      .demo-slide-grid {
        display: grid;
        grid-template-columns: 1.05fr 0.95fr;
        gap: 28px;
        align-items: end !important;
      }
      .demo-wrap {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        gap: 0;
      }

      /* Slide 10 Right Calculator & 3 Left Boxes Aligned Top & Bottom */
      .calc-grid-layout {
        display: grid;
        grid-template-columns: 1.18fr 0.82fr;
        gap: 24px;
        align-items: stretch !important;
      }
      .calc-side-stack {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 14px;
        height: 100%;
      }
      .calc-side-card {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 22px 26px !important;
      }
      .calc-side-card h3 {
        font-size: clamp(19px, 1.55vw, 23px) !important;
      }

      /* Slide 19 Enlarged User Experience Box */
      .ux-flow-card {
        padding: 24px 28px !important;
      }
      .ux-step-pill {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.16);
        padding: 12px 20px;
        border-radius: 14px;
        font-size: 15.5px;
        font-weight: 900;
        color: #ffffff;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
      }
      .ux-step-pill.ux-step-final {
        background: var(--persian-green);
        color: #0b0f13;
        border-color: var(--persian-green);
        box-shadow: 0 8px 22px var(--persian-green-glow);
      }
      .ux-step-arrow {
        font-size: 24px;
        font-weight: 900;
        color: var(--persian-green);
        line-height: 1;
      }

      /* Slide 21 Enlarged 5 Bottom Pillars */
      .why-ewano-5grid {
        gap: 16px !important;
      }
      .why-pillar-card {
        padding: 22px 18px !important;
        text-align: center;
        min-height: 96px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }
      .why-pillar-title {
        font-size: 22px !important;
        font-weight: 900 !important;
        letter-spacing: -0.2px;
      }
      .why-pillar-desc {
        font-size: 14.5px !important;
        font-weight: 700 !important;
        color: #e2e8f0 !important;
        line-height: 1.65 !important;
      }

      /* =========================================================================
       MOBILE RESPONSIVE DESIGN (Reference Viewport: 412 x 917 px)
       ========================================================================= */
      @media (max-width: 768px) {
        html,
        body {
          width: 100vw;
          height: 100dvh;
          overflow: hidden;
        }

        /* Compact Mobile Header (54px) */
        .deck-header {
          height: 54px;
          padding: 0 12px;
        }
        .brand-cluster {
          gap: 8px;
        }
        .logo-mark {
          width: 34px;
          height: 34px;
          border-radius: 9px;
        }
        .brand-titles .main-title {
          font-size: 13.5px;
        }
        .brand-titles .main-title span:nth-child(2) {
          display: none;
        }
        .brand-titles .sub-title {
          font-size: 9.5px;
        }
        .co-pill,
        .chapter-nav {
          display: none !important;
        }
        .header-actions {
          gap: 6px;
        }
        .icon-btn {
          height: 32px;
          padding: 0 10px;
          font-size: 11px;
          border-radius: 8px;
        }

        /* Slide Stage with smooth vertical scroll for 412x917 */
        .stage-container {
          top: 54px;
          bottom: 54px;
        }
        .slide {
          padding: 16px 14px 28px !important;
          justify-content: flex-start !important;
          overflow-y: auto !important;
          -webkit-overflow-scrolling: touch;
        }
        .slide-inner {
          height: auto !important;
          min-height: min-content;
          justify-content: flex-start !important;
          gap: 14px !important;
          padding-bottom: 16px;
        }

        /* Typography scaled for 412px width */
        .slide-top-meta {
          gap: 8px;
        }
        .eyebrow-badge {
          font-size: 10.5px;
          padding: 4px 10px;
        }
        .slide-headline,
        h1.slide-headline {
          font-size: 21px !important;
          line-height: 1.38 !important;
        }
        .slide-subtitle {
          font-size: 12.5px !important;
          line-height: 1.65 !important;
        }
        .glass-card {
          padding: 15px 16px !important;
          border-radius: 16px !important;
        }
        .glass-card h3 {
          font-size: 16.5px !important;
        }
        .glass-card h4,
        .service-tile h4 {
          font-size: 14.5px !important;
        }

        /* Single-column / 2-column grids on 412px mobile */
        .grid-2,
        .grid-2-asym,
        .grid-3,
        .grid-4,
        .grid-5,
        .ecosystem-layout,
        .step-hero-panel,
        .calc-grid-layout,
        .demo-slide-grid,
        .network-map-grid {
          grid-template-columns: 1fr !important;
          gap: 12px !important;
        }
        .companies-grid {
          grid-template-columns: repeat(2, 1fr) !important;
          gap: 8px !important;
        }
        .services-10-grid,
        .brands-25-grid {
          grid-template-columns: repeat(2, 1fr) !important;
          gap: 10px !important;
        }

        /* Slide 1 4-Cards Stage adapted for 412px width */
        .hero-cards-stage {
          height: 340px !important;
          margin-top: 6px;
          transform: scale(0.84);
          transform-origin: center center;
        }
        .ewano-3d-card {
          width: 280px !important;
          height: 168px !important;
          padding: 16px 18px !important;
        }
        .ewano-3d-card.card-welfare {
          transform: translate3d(-45px, -85px, 10px) rotate(-7deg) !important;
        }
        .ewano-3d-card.card-credit {
          transform: translate3d(-15px, -30px, 30px) rotate(-2deg) !important;
        }
        .ewano-3d-card.card-cash {
          transform: translate3d(15px, 25px, 50px) rotate(3deg) !important;
        }
        .ewano-3d-card.card-debit-black {
          transform: translate3d(45px, 80px, 70px) rotate(7deg) !important;
        }

        /* Journey Progress Rail on Mobile (2x3 Grid) */
        .journey-progress-rail {
          grid-template-columns: repeat(2, 1fr) !important;
          gap: 6px !important;
          padding: 10px !important;
        }
        .rail-step {
          padding: 6px 8px !important;
        }
        .rail-num {
          width: 24px !important;
          height: 24px !important;
          font-size: 11.5px !important;
        }
        .rail-label {
          font-size: 11px !important;
        }

        /* Calculator on 412px Mobile */
        .calc-inputs {
          padding: 14px 16px !important;
          gap: 12px !important;
        }
        .calc-amount {
          font-size: 17px !important;
        }
        .calc-ticks b {
          font-size: 9.5px !important;
        }
        .calc-result {
          grid-template-columns: 1fr !important;
          padding: 16px !important;
          gap: 12px !important;
        }
        .calc-res-main b {
          font-size: 24px !important;
        }
        .calc-res-list {
          border-right: none !important;
          padding-right: 0 !important;
          border-top: 1px solid rgba(255, 255, 255, 0.12);
          padding-top: 12px;
        }

        /* Phone Mockup on 412px Mobile */
        .phone {
          width: 100% !important;
          max-width: 356px !important;
          height: 560px !important;
          margin: 0 auto;
        }
        .demo-tabs {
          gap: 4px !important;
        }
        .demo-tab {
          padding: 5px 10px !important;
          font-size: 11px !important;
        }

        /* Slide 19 UX Flow Steps on Mobile */
        .ux-flow-card {
          padding: 16px !important;
        }
        .ux-flow-steps {
          gap: 6px !important;
          justify-content: center !important;
        }
        .ux-step-pill {
          padding: 8px 12px !important;
          font-size: 12.5px !important;
        }
        .ux-step-arrow {
          font-size: 16px !important;
        }

        /* Slide 20 Iran Map on
```

=== ./index2.html (ادامه 2) ===

```
 Mobile */
        .imap-svg {
          max-height: 260px !important;
        }

        /* Slide 21 Why Ewano Pillars on Mobile */
        .why-pillar-card {
          padding: 16px 14px !important;
          min-height: auto !important;
        }
        .why-pillar-title {
          font-size: 18px !important;
        }
        .why-pillar-desc {
          font-size: 13px !important;
        }

        /* Compact Mobile Footer (54px) */
        .deck-footer {
          height: 54px;
          padding: 0 12px;
        }
        .nav-controls {
          width: 100%;
          justify-content: space-between;
          gap: 8px;
        }
        .nav-arrow-btn {
          height: 36px;
          padding: 0 12px;
          font-size: 12px;
        }
        .slide-counter-pill {
          padding: 5px 12px;
          font-size: 12px;
        }
        .slide-dots,
        .deck-footer > div:last-child {
          display: none !important;
        }
      }

      /* Touch / Click Expand State for Mobile & Tablet */
      .glass-card.expanded-box p,
      .glass-card.expanded-box ul,
      .glass-card.expanded-box .hover-reveal,
      .service-tile.expanded-box p {
        max-height: 420px !important;
        opacity: 1 !important;
        transform: translateY(0) !important;
        margin-top: 8px !important;
      }

      /* Exact 412x917 Mobile Viewport Optimizations */
      @media (max-width: 480px) {
        .deck-header {
          height: 50px !important;
          padding: 0 10px !important;
        }
        .stage-container {
          top: 50px !important;
          bottom: 52px !important;
        }
        .deck-footer {
          height: 52px !important;
          padding: 0 10px !important;
        }
        .slide {
          padding: 14px 12px 24px !important;
        }
        .slide-headline,
        h1.slide-headline {
          font-size: 19.5px !important;
          line-height: 1.35 !important;
        }
        .hero-cards-stage {
          height: 310px !important;
          transform: scale(0.78) !important;
        }
        .phone {
          max-width: 344px !important;
          height: 540px !important;
        }
      }

      /* =========================================================================
       USER REQUEST UPDATES (1 - 13)
       ========================================================================= */

      /* Item 4: Larger and more readable hover text across all cards */
      .glass-card p,
      .glass-card ul,
      .glass-card .hover-reveal,
      .service-tile p,
      .step-hero-panel p,
      .calc-side-card p {
        font-size: 14.5px !important;
        line-height: 1.85 !important;
        color: #e2e8f0 !important;
      }
      .glass-card:not(.no-collapse):hover p,
      .glass-card:not(.no-collapse):hover ul,
      .glass-card:not(.no-collapse):hover .hover-reveal,
      .service-tile:hover p {
        max-height: 480px !important;
      }

      /* Item 8: Larger and more readable fonts in Chapter 2 (Credit Journey Slides 11 to 16) */
      .slide[data-chapter='2'] p {
        font-size: 16.5px !important;
        line-height: 2 !important;
      }
      .slide[data-chapter='2'] .grid-2 div,
      .slide[data-chapter='2'] .grid-3 div,
      .slide[data-chapter='2'] ul li {
        font-size: 14.5px !important;
        line-height: 1.9 !important;
      }
      .slide[data-chapter='2'] h2 {
        font-size: clamp(26px, 2.4vw, 34px) !important;
      }
      .rail-step .rail-label {
        font-size: 13.5px !important;
        font-weight: 800 !important;
      }
      .rail-num {
        width: 32px !important;
        height: 32px !important;
        font-size: 14px !important;
      }

      /* Item 3: Debit Card Flip (Front & Back) on Slide 1 */
      .ewano-3d-card.card-debit-black {
        perspective: 1200px;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
      }
      .debit-flipper-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.75s cubic-bezier(0.2, 0.9, 0.3, 1.15);
        transform-style: preserve-3d;
        border-radius: 22px;
        box-shadow:
          0 24px 50px rgba(0, 0, 0, 0.7),
          0 0 0 1.5px rgba(255, 255, 255, 0.25);
      }
      .ewano-3d-card.card-debit-black.is-flipped .debit-flipper-inner {
        transform: rotateY(180deg);
        box-shadow:
          0 28px 60px rgba(0, 212, 180, 0.4),
          0 0 0 2px var(--persian-green);
      }
      .debit-side {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        -webkit-backface-visibility: hidden;
        border-radius: 22px;
        overflow: hidden;
      }
      .debit-back {
        transform: rotateY(180deg);
      }

      /* Item 5: Slide 2 Company Logo Slots & Larger Diagram */
      .comp-logo-box {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.14);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        padding: 4px;
        overflow: hidden;
      }
      .comp-logo-box img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        display: block;
      }
      .comp-logo-box.placeholder-logo {
        font-size: 16px;
        font-weight: 900;
        color: var(--persian-green);
        background: rgba(0, 212, 180, 0.12);
        border-color: rgba(0, 212, 180, 0.3);
      }
      .company-pill {
        gap: 12px !important;
        padding: 8px 12px !important;
        font-size: 13.5px !important;
      }
      .comp-name {
        font-weight: 800;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .slide[data-chapter='0'] .ecosystem-layout {
        grid-template-columns: 1.12fr 0.88fr !important;
      }
      .slide[data-chapter='0'] svg text {
        font-size: 13px !important;
      }

      /* Item 7: Slide 5 Brand Logo Slots */
      .brand-logo-slot {
        width: 32px;
        height: 32px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(255, 255, 255, 0.25);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        padding: 3px;
        margin-left: 8px;
        overflow: hidden;
      }
      .brand-logo-slot img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        display: block;
      }
      .brand-logo-slot.placeholder-brand {
        background: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        font-size: 14px;
        font-weight: 900;
      }
      .brand-tile {
        padding: 10px 12px !important;
      }
      .brand-tile-name {
        flex: 1;
        font-size: 13.5px !important;
      }

      /* Item 13: iPhone 18 Pro Max Frame */
      .iphone-18-pro-max {
        width: 340px;
        height: 650px;
        background: #000000;
        border-radius: 52px;
        padding: 12px;
        box-shadow:
          0 0 0 3px #3d3d42,
          0 0 0 5px #1c1c1e,
          0 30px 75px rgba(0, 0, 0, 0.85),
          0 0 36px rgba(0, 212, 180, 0.25);
        position: relative;
        display: flex;
        flex-direction: column;
        flex-shrink: 0;
      }
      .iphone-dynamic-island {
        position: absolute;
        top: 18px;
        left: 50%;
        transform: translateX(-50%);
        width: 108px;
        height: 28px;
        background: #000000;
        border-radius: 20px;
        z-index: 20;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 12px;
        box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.08);
        pointer-events: none;
      }
      .island-camera {
        width: 11px;
        height: 11px;
        border-radius: 50%;
        background: #111422;
        box-shadow: inset 0 0 3px rgba(0, 147, 221, 0.6);
      }
      .island-sensor {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #0a0d15;
      }
      .iphone-screen-wrap {
        width: 100%;
        height: 100%;
        background: #ffffff;
        border-radius: 42px;
        overflow: hidden;
        position: relative;
      }
      .iphone-pwa-iframe {
        width: 100%;
        height: 100%;
        border: none;
        display: block;
        background: #ffffff;
      }

      /* Item 9: Slide 17 Welfare Categories & Brand Pills with Logo */
      .welfare-categories-strip {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
      }
      .welfare-cat-pill {
        background: rgba(0, 212, 180, 0.14);
        border: 1.5px solid var(--border-green);
        color: #ffffff;
        padding: 10px 22px;
        border-radius: 99px;
        font-weight: 800;
        font-size: 15px;
        transition: all 0.25s ease;
      }
      .welfare-cat-pill.wcat-active {
        background: var(--persian-green);
        color: #0b0f13;
        font-weight: 900;
        box-shadow: 0 4px 16px var(--persian-green-glow);
      }
      .welfare-cat-pill.wcat-orange {
        background: rgba(255, 119, 34, 0.16);
        border-color: rgba(255, 119, 34, 0.45);
        color: var(--persian-orange);
      }
      .welfare-cat-pill.wcat-muted {
        background: rgba(255, 255, 255, 0.06);
        border-color: var(--border-glass);
        color: #cbd5e1;
      }
      .welfare-card-large {
        padding: 24px 22px !important;
        border-radius: 20px !important;
      }
      .brand-logo-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 14px !important;
        border-radius: 12px !important;
        font-size: 13.5px !important;
        font-weight: 800;
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(255, 255, 255, 0.14) !important;
      }
      .pill-brand-logo {
        width: 24px;
        height: 24px;
        object-fit: contain;
        background: #ffffff;
        border-radius: 6px;
        padding: 2px;
      }
      .pill-brand-placeholder {
        width: 24px;
        height: 24px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: rgba(0, 212, 180, 0.2);
        color: var(--persian-green);
        border-radius: 6px;
        font-size: 12px;
        font-weight: 900;
      }

      /* Item 11: Marquee LTR animation with fade edges & Rich Map Popup */
      .marquee-fade-wrapper {
        position: relative;
        overflow: hidden;
        width: 100%;
        -webkit-mask-image: linear-gradient(
          90deg,
          transparent 0%,
          #000 8%,
          #000 92%,
          transparent 100%
        );
        mask-image: linear-gradient(
          90deg,
          transparent 0%,
          #000 8%,
          #000 92%,
          transparent 100%
        );
      }
      .logo-dots.lm-ltr .lm-track {
        display: flex;
        width: max-content;
        animation: lm-slide-ltr 42s linear infinite !important;
      }
      @keyframes lm-slide-ltr {
        from {
          transform: translateX(50%);
        }
        to {
          transform: translateX(0);
        }
      }
      .imap-tip-rich {
        position: absolute;
        z-index: 50;
        pointer-events: none;
        background: rgba(14, 19, 24, 0.96);
        border: 1.5px solid var(--persian-green);
        border-radius: 14px;
        box-shadow: 0 16px 36px rgba(0, 0, 0, 0.85);
        padding: 12px 16px;
        color: #ffffff;
        opacity: 0;
        transform: translate(-50%, calc(-100% - 14px));
        transition:
          opacity 0.2s ease,
          transform 0.2s ease;
        white-space: nowrap;
        min-width: 170px;
      }
      .imap-tip-rich.show {
        opacity: 1;
      }
      .tip-title-row {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        gap: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
        padding-bottom: 6px;
        margin-bottom: 6px;
      }
      .tip-prov-name {
        font-size: 15px;
        font-weight: 900;
        color: #ffffff;
      }
      .tip-city-name {
        font-size: 11.5px;
        font-weight: 700;
        color: var(--persian-green);
      }
      .tip-merch-row {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        font-weight: 800;
        color: #cbd5e1;
      }
      .tip-merch-num {
        color: var(--persian-green);
        font-size: 15px;
        font-weight: 900;
      }

      /* Item 12: Client Org Frames with Logo Slots */
      .client-org-frame {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 14px;
        padding: 10px 14px;
        display: flex;
        align-items: center;
        gap: 12px;
        transition: all 0.25s ease;
      }
      .client-org-frame:hover {
        border-color: var(--persian-green);
        background: var(--persian-green-soft);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 212, 180, 0.15);
      }
      .client-logo-box {
        width: 36px;
        height: 36px;
        border-radius: 9px;
        background: rgba(255, 255, 255, 0.92);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        padding: 4px;
        overflow: hidden;
      }
      .client-logo-box img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        display: block;
      }
      .client-logo-box.placeholder-client {
        background: rgba(0, 212, 180, 0.14);
        color: var(--persian-green);
        font-size: 15px;
        font-weight: 900;
      }
      .client-org-name {
        font-size: 13.5px;
        font-weight: 800;
        color: #f1f5f9;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }

      /* =========================================================================
       ADDITIONAL REFINEMENTS CSS
       ========================================================================= */

      /* Item 2: Mobile Header Buttons - hide text, keep only hamburger icon */
      @media (max-width: 768px) {
        .header-actions .icon-btn[onclick='toggleFullScreen()'] {
          display: none !important;
        }
        .header-actions .icon-btn[onclick='toggleDrawer()'] span {
          display: none !important;
        }
        .header-actions .icon-btn[onclick='toggleDrawer()'] {
          width: 38px !important;
          height: 38px !important;
          padding: 0 !important;
          justify-content: center;
          border-radius: 10px !important;
        }
      }

      /* Item 3: Card-specific hover shadows matching card colors */
      .ewano-3d-card.card-welfare:hover {
        box-shadow: 0 30px 65px rgba(0, 147, 221, 0.55) !important;
      }
      .ewano-3d-card.card-credit:hover {
        box-shadow: 0 30px 65px rgba(255, 119, 34, 0.55) !important;
      }
      .ewano-3d-card.card-cash:hover {
        box-shadow: 0 30px 65px rgba(0, 212, 180, 0.55) !important;
      }
      .glass-card[style*='border-top:4px solid var(--sky-blue)']:hover,
      .glass-card[style*='border-top:5px solid var(--sky-blue)']:hover,
      .glass-card[style*='border-right:4px solid var(--sky-blue)']:hover,
      .glass-card[style*='border-right:5px solid var(--sky-blue)']:hover,
      .glass-card[style*='border-right:6px solid var(--sky-blue)']:hover,
      #balCard-welfare:hover {
        border-color: var(--sky-blue) !important;
        box-shadow: 0 20px 48px rgba(0, 147, 221, 0.3) !important;
      }
      .glass-card[style*='border-top:4px solid var(--persian-orange)']:hover,
      .glass-card[style*='border-top:5px solid var(--persian-orange)']:hover,
      .glass-card[style*='border-right:4px solid var(--persian-orange)']:hover,
      .glass-card[style*='border-right:5px solid var(--persian-orange)']:hover,
      .glass-card[style*='border-right:6px solid var(--persian-orange)']:hover,
      #balCard-credit:hover {
        border-color: var(--persian-orange) !important;
        box-shadow: 0 20px 48px rgba(255, 119, 34, 0.3) !important;
      }
      .glass-card[style*='border-top:4px solid var(--persian-green)']:hover,
      .glass-card[style*='border-top:5px solid var(--persian-green)']:hover,
      .glass-card[style*='border-right:4px solid var(--persian-green)']:hover,
      .glass-card[style*='border-right:5px solid var(--persian-green)']:hover,
      .glass-card[style*='border-right:6px solid var(--persian-green)']:hover,
      #balCard-cash:hover {
        border-color: var(--persian-green) !important;
        box-shadow: 0 20px 48px rgba(0, 212, 180, 0.3) !important;
      }
      .glass-card[style*='border-right:4px solid #A78BFA']:hover,
      .glass-card[style*='border-right:5px solid #A78BFA']:hover,
      .glass-card[style*='border-top:4px solid #A78BFA']:hover {
        border-color: #a78bfa !important;
        box-shadow: 0 20px 48px rgba(167, 139, 250, 0.3) !important;
      }

      /* Item 4: White background for ALL logo boxes across all pages */
      .comp-logo-box,
      .brand-logo-slot,
      .pill-brand-logo,
      .client-circle-logo,
      .client-logo-box,
      .logo-dot {
        background: #ffffff !important;
      }

      /* Item 4: Slide 2 Equal 3-Columns in Companies Grid */
      .slide[data-chapter='0'] .companies-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 10px !important;
      }
      .slide[data-chapter='0'] .companies-grid .company-pill {
        height: 52px;
        box-sizing: border-box;
      }

      /* Item 6: Slide 5 2X Larger Tiles, Texts and Logos */
      .brands-25-grid {
        display: grid !important;
        grid-template-columns: repeat(5, 1fr) !important;
        gap: 16px !important;
      }
      .brands-25-grid .brand-tile {
        padding: 16px 18px !important;
        border-radius: 18px !important;
        min-height: 72px;
      }
      .brands-25-grid .brand-logo-slot {
        width: 52px !important;
        height: 52px !important;
        border-radius: 14px !important;
        padding: 6px !important;
        margin-left: 14px !important;
      }
      .brands-25-grid .brand-tile-name {
        font-size: 18px !important;
        font-weight: 900 !important;
      }
      .brands-25-grid .brand-tile-cat {
        font-size: 13px !important;
        padding: 4px 10px !important;
        border-radius: 10px !important;
      }

      /* Item 7: Slide 8 iPhone Frame Max-Width 608px & Alignment */
      .iphone-18-pro-max {
        width: 100% !important;
        max-width: 608px !important;
        height: 720px !important;
        aspect-ratio: 440 / 956;
        border-radius: 54px !important;
        padding: 12px !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-slide-grid {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 32px !important;
        align-items: stretch !important;
        margin-top: 10px !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        height: 90% !important;
        gap: 16px !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 24px 28px !important;
      }

      /* Item 8: Slide 10 Full Height Hover Expand */
      .calc-side-card:hover p {
        max-height: 500px !important;
      }

      /* Item 9: Chapter 3 6-Step Visual Box Texts 2X Larger */
      .step-visual-box {
        padding: 32px 24px !important;
      }
      .step-visual-box text {
        font-size: 16px !important;
      }
      .step-visual-box div:nth-of-type(1) {
        font-size: 20px !important;
        font-weight: 900 !important;
        margin-top: 14px !important;
      }
      .step-visual-box div:nth-of-type(2) {
        font-size: 15px !important;
        font-weight: 700 !important;
        margin-top: 6px !important;
      }

      /* Item 14: Slide 18 Vertical Floating Voucher Cards with 3D Flip */
      .voucher-card-item {
        position: absolute;
        width: 220px;
        height: 330px;
        perspective: 1200px;
        cursor: pointer;
        transition:
          transform 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          z-index 0.45s ease;
      }
      .vcard-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.75s cubic-bezier(0.2, 0.9, 0.3, 1.15);
        transform-style: preserve-3d;
        border-radius: 20px;
        box-shadow:
          0 24px 50px rgba(0, 0, 0, 0.65),
          0 0 0 1.5px rgba(255, 255, 255, 0.22);
      }
      .voucher-card-item.is-flipped .vcard-inner {
        transform: rotateY(180deg);
        box-shadow:
          0 28px 60px rgba(0, 212, 180, 0.45),
          0 0 0 2px var(--persian-green);
      }
      .vcard-side {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        -webkit-backface-visibility: hidden;
        border-radius: 20px;
        overflow: hidden;
        background: #171f26;
      }
      .vcard-side img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
      }
      .vcard-back {
        transform: rotateY(180deg);
      }

      /* Layout order: Right to Left (vc-card-1 = 3M, vc-card-2 = 5M, vc-card-3 = 10M) */
      .vc-card-1 {
        transform: translate3d(85px, 25px, 20px) rotate(6deg);
        z-index: 3;
      }
      .vc-card-2 {
        transform: translate3d(0, -10px, 45px) rotate(0deg);
        z-index: 4;
      }
      .vc-card-3 {
        transform: translate3d(-85px, 25px, 10px) rotate(-6deg);
        z-index: 2;
      }
      .vc-card-1:hover {
        z-index: 10 !important;
        transform: translate3d(85px, 8px, 90px) rotate(0deg) scale(1.06) !important;
      }
      .vc-card-2:hover {
        z-index: 10 !important;
        transform: translate3d(0, -22px, 100px) rotate(0deg) scale(1.06) !important;
      }
      .vc-card-3:hover {
        z-index: 10 !important;
        transform: translate3d(-85px, 8px, 90px) rotate(0deg) scale(1.06) !important;
      }

      /* Item 16: Slide 20 Value Card Hover Expansion */
      .s20-value-card:hover .s20-val-reveal {
        max-height: 500px !important;
        opacity: 1 !important;
        margin-top: 12px !important;
      }

      /* Item 17: Slide 21 Marquee Section Overflow None */
      .marquee-fade-wrapper,
      .marquee-fade-wrapper .logo-dots {
        overflow: visible !important;
        mask-image: none !important;
        -webkit-mask-image: none !important;
      }

      /* Item 18: Slide 22 Dual-Row Infinite Clients Marquee */
      .client-marquee-wrapper {
        position: relative;
        overflow: hidden;
        width: 100%;
        padding: 10px 0;
        display: flex;
        flex-direction: column;
        gap: 16px;
        -webkit-mask-image: linear-gradient(
          90deg,
          transparent 0%,
          #000 7%,
          #000 93%,
          transparent 100%
        );
        mask-image: linear-gradient(
          90deg,
          transparent 0%,
          #000 7%,
          #000 93%,
          transparent 100%
        );
      }
      .client-track-container {
        overflow: hidden;
        width: 100%;
      }
      .client-track {
        display: flex;
        width: max-content;
      }
      .client-set {
        display: flex;
        gap: 20px;
        padding-inline-end: 20px;
        padding-top: 16px;
      }
      .track-move-right {
        animation: clientScrollRight 38s linear infinite;
      }
      .track-move-left {
        animation: clientScrollLeft 38s linear infinite;
      }
      .client-marquee-wrapper:hover .client-track {
        animation-play-state: paused;
      }
      @keyframes clientScrollRight {
        from {
          transform: translateX(50%);
        }
        to {
          transform: translateX(0);
        }
      }
      @keyframes clientScrollLeft {
        from {
          transform: translateX(0);
        }
        to {
          transform: translateX(-50%);
        }
      }
      .client-org-unit {
        width: 180px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 8px;
        flex-shrink: 0;
      }
      .client-circle-logo {
        width: 68px;
        height: 68px;
        border-radius: 50%;
        background: #ffffff !important;
        border: 2px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 22px rgba(0, 0, 0, 0.45);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 8px;
        overflow: hidden;
        transition:
          transform 0.25s ease,
          border-color 0.25s ease;
      }
      .client-org-unit:hover .client-circle-logo {
        transform: scale(1.12);
        border-color: var(--persian-green);
        box-shadow: 0 12px 28px rgba(0, 212, 180, 0.35);
      }
      .client-circle-logo img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        display: block;
      }
      .client-circle-logo.placeholder-circle {
        background: rgba(0, 212, 180, 0.15) !important;
        color: var(--persian-green);
        font-size: 24px;
        font-weight: 900;
      }
      .client-unit-name {
        font-size: 13.5px;
        font-weight: 800;
        color: #e2e8f0;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 100%;
      }

      /* === 1. FOOTER PILL EXACT MATCH === */
      .slide-counter-pill {
        height: 40px !important;
        padding: 0 18px !important;
        border-radius: 12px !important;
        font-size: 13px !important;
        font-weight: 800 !important;
        color: #e2e8f0 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-sizing: border-box !important;
        gap: 8px !important;
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid var(--border-glass) !important;
      }
      .nav-arrow-btn {
        height: 40px !important;
        padding: 0 18px !important;
        border-radius: 12px !important;
        box-sizing: border-box !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
      }

      /* === 2. PER-CARD HOVER SHADOWS MATCHING CARD ACCENT COLOR === */
      .glass-card {
        transition:
          transform var(--transition-normal),
          box-shadow var(--transition-normal),
          border-color var(--transition-normal) !important;
      }
      /* Orange Cards */
      .glass-card[style*='--persian-orange']:hover,
      .glass-card[style*='#FF7722']:hover,
      .glass-card.orange-hover:hover,
      .card-orange:hover,
      .card-credit:hover {
        box-shadow:
          0 20px 45px rgba(255, 119, 34, 0.4),
          0 0 0 1px rgba(255, 119, 34, 0.5) !important;
        border-color: var(--persian-orange) !important;
      }
      /* Blue Cards */
      .glass-card[style*='--sky-blue']:hover,
      .glass-card[style*='#0093DD']:hover,
      .glass-card.blue-hover:hover,
      .card-blue:hover,
      .card-welfare:hover {
        box-shadow:
          0 20px 45px rgba(0, 147, 221, 0.4),
          0 0 0 1px rgba(0, 147, 221, 0.5) !important;
        border-color: var(--sky-blue) !important;
      }
      /* Green Cards */
      .glass-card[style*='--persian-green']:hover,
      .glass-card[style*='#00D4B4']:hover,
      .glass-card.green-hover:hover,
      .card-green:hover,
      .card-cash:hover {
        box-shadow:
          0 20px 45px rgba(0, 212, 180, 0.4),
          0 0 0 1px rgba(0, 212, 180, 0.5) !important;
        border-color: var(--persian-green) !important;
      }
      /* Purple Cards */
      .glass-card[style*='#A78BFA']:hover,
      .glass-card[style*='rgba(111,89,169']:hover,
      .glass-card.purple-hover:hover {
        box-shadow:
          0 20px 45px rgba(167, 139, 250, 0.4),
          0 0 0 1px rgba(167, 139, 250, 0.5) !important;
        border-color: #a78bfa !important;
      }
      /* Default cards */
      .glass-card:not([style*='--persian-orange']):not(
          [style*='--sky-blue']
        ):not([style*='--persian-green']):not([style*='#A78BFA']):hover {
        box-shadow:
          0 20px 45px rgba(0, 0, 0, 0.5),
          0 0 0 1px rgba(255, 255, 255, 0.25) !important;
      }

      /* === SLIDE 2 LOGO BOXES 2X & EQUAL 3 COLUMNS === */
      .companies-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 12px !important;
      }
      .company-pill {
        height: 100% !important;
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        padding: 10px 14px !important;
        box-sizing: border-box !important;
      }
      .comp-logo-box {
        width: 76px !important;
        height: 44px !important;
        min-width: 76px !important;
        border-radius: 10px !important;
        background: #ffffff !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 4px 8px !important;
        box-sizing: border-box !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
      }
      .comp-logo-box img {
        max-width: 100% !important;
        max-height: 100% !important;
        width: auto !important;
        height: auto !important;
        object-fit: contain !important;
      }

      /* === SLIDE 5 SINGLE LINE TITLES & BADGES === */
      .brand-tile-2x .brand-name {
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 15px !important;
        font-weight: 900 !important;
        text-align: center !important;
      }
      .brand-tile-2x .brand-cat-badge {
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        margin-top: 4px !important;
        text-align: center !important;
      }

      /* === SLIDE 10 HOVER DESCRIPTIONS FULL DISPLAY === */
      .calc-side-card {
        transition: all var(--transition-normal) !important;
      }
      .calc-side-card .hover-desc-reveal {
        max-height: 0;
        opacity: 0;
        overflow: hidden;
        transition:
          max-height 0.4s ease,
          opacity 0.3s ease;
      }
      .calc-side-card:hover .hover-desc-reveal {
        max-height: 600px !important;
        opacity: 1 !important;
        overflow: visible !important;
      }

      /* === SLIDE 19 TOP 3 CARDS EQUAL BEFORE HOVER === */
      .s20-top-cards {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        align-items: stretch !important;
      }
      .s20-top-cards .glass-card {
        min-height: 250px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        height: 100% !important;
        box-sizing: border-box !important;
      }
      .s20-value-card {
        min-height: 250px !important;
        max-height: 250px !important;
        overflow: hidden !important;
        transition:
          max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          box-shadow 0.3s ease !important;
      }
      .s20-value-card:hover {
        max-height: 680px !important;
        overflow: visible !important;
        z-index: 10 !important;
      }

      /* === SLIDE 20 MARQUEE FADE SIDES === */
      .marquee-fade-wrapper {
        position: relative !important;
        overflow: hidden !important;
        -webkit-mask-image: linear-gradient(
          to right,
          transparent 0%,
          black 7%,
          black 93%,
          transparent 100%
        ) !important;
        mask-image: linear-gradient(
          to right,
          transparent 0%,
          black 7%,
          black 93%,
          transparent 100%
        ) !important;
      }

      /* === SLIDE 21 ROW 2 LEFT TO RIGHT LOOP === */
      @keyframes clientScrollLeftToRight {
        0% {
          transform: translateX(-50%);
        }
        100% {
          transform: translateX(0%);
        }
      }
      .client-track-reverse {
        display: flex !important;
        gap: 18px !important;
        width: max-content !important;
        animation: clientScrollLeftToRight 28s linear infinite !important;
      }
      .client-track-reverse:hover {
        animation-play-state: paused !important;
      }

      /* Slide 8 Mockup 19.5:9 ratio & +20% dimensions */
      .iphone-18-pro-max {
        width: 100% !important;
        max-width: 440px !important;
        aspect-ratio: 9 / 19.5 !important;
        margin: 0 16px !important;
        position: relative !important;
        border: 11px solid #1f2933 !important;
        border-radius: 52px !important;
        box-shadow:
          0 30px 80px rgba(0, 0, 0, 0.8),
          0 0 0 2px rgba(255, 255, 255, 0.12) !important;
        overflow: hidden !important;
        background: #000000 !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .iphone-screen-wrap {
        flex: 1 !important;
        width: 100% !important;
        height: 100% !important;
        position: relative !important;
        overflow: hidden !important;
      }
      .iphone-pwa-iframe {
        width: 100% !important;
        height: 100% !important;
        border: none !important;
      }

      /* 3 Balance Boxes under Headline: Half Height & Centered Vertically */
      .demo-slide-grid {
        display: grid !important;
        grid-template-columns: 1fr 0.95fr !important;
        gap: 28px !important;
        align-items: center !important;
      }
      .demo-left-col {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        gap: 14px !important;
      }
      .demo-left-col .glass-card {
        padding: 12px 18px !important;
      }
      .demo-left-col .glass-card h3 {
        font-size: 16px !important;
        margin: 0 !important;
      }
      .demo-left-col .glass-card p {
        font-size: 12.5px !important;
        line-height: 1.6 !important;
        margin-top: 5px !important;
        margin-bottom: 0 !important;
      }

      /* === SLIDE 5: 1-LINE TITLE & 1-LINE BADGE BELOW === */
      .brands-25-grid {
        display: grid !important;
        grid-template-columns: repeat(5, 1fr) !important;
        gap: 14px !important;
      }
      .brand-tile {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 12px 8px !important;
        box-sizing: border-box !important;
        text-align: center !important;
        border-radius: 16px !important;
        min-height: 135px !important;
      }
      .brand-logo-slot {
        width: 58px !important;
        height: 58px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background: #ffffff !important;
        border-radius: 14px !important;
        padding: 6px !important;
        box-sizing: border-box !important;
        margin-bottom: 8px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
      }
      .brand-logo-slot img {
        max-width: 100% !important;
        max-height: 100% !important;
        width: auto !important;
        height: auto !important;
        object-fit: contain !important;
      }
      .brand-tile-name {
        display: block !important;
        width: 100% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 14.5px !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-align: center !important;
        line-height: 1.35 !important;
        margin: 0 !important;
      }
      .brand-tile-cat {
        display: inline-block !important;
        max-width: 90% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        background: rgba(255, 255, 255, 0.08) !important;
        padding: 2px 10px !important;
        border-radius: 99px !important;
        text-align: center !important;
        margin-top: 5px !important;
        line-height: 1.4 !important;
      }

      /* === SLIDE 8: IPHONE 18 PRO MAX RATIO WITHOUT DYNAMIC ISLAND === */
      .iphone-dynamic-island {
        display: none !important;
      }
      .iphone-18-pro-max {
        width: 100% !important;
        max-width: 410px !important;
        aspect-ratio: 9 / 19.5 !important;
        margin: 0 16px !important;
        position: relative !important;
        border: 10px solid #1f2933 !important;
        border-radius: 48px !important;
        box-shadow:
          0 30px 80px rgba(0, 0, 0, 0.85),
          0 0 0 2px rgba(255, 255, 255, 0.12) !important;
        overflow: hidden !important;
        background: #000000 !important;
        display: flex !important;
        flex-direction: column !important;
      }

      /* 3 Balance Boxes: Half Height, Bold & Larger Titles matching other slides */
      .demo-slide-grid {
        display: grid !important;
        grid-template-columns: 1fr 0.95fr !important;
        gap: 26px !important;
        align-items: center !important;
      }
      .demo-left-col {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        gap: 12px !important;
      }
      .demo-left-col .glass-card {
        padding: 12px 20px !important;
        border-radius: 16px !important;
      }
      .demo-left-col .glass-card h3 {
        font-size: 19px !important;
        font-weight: 900 !important;
        margin: 0 0 4px 0 !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
      }
      .demo-left-col .glass-card p {
        font-size: 12.5px !important;
        line-height: 1.6 !important;
        color: #cbd5e1 !important;
        margin: 0 !important;
      }

      /* === SLIDE 10: FULL UNCLIPPED HOVER DESCRIPTIONS === */
      .calc-side-stack {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        gap: 14px !important;
        height: 100% !important;
        position: relative !important;
      }
      .calc-side-card {
        position: relative !important;
        transition:
          transform var(--transition-normal),
          box-shadow var(--transition-normal),
          background 0.3s ease !important;
        overflow: hidden !important;
        border-radius: 18px !important;
        padding: 18px 22px !important;
      }
      .calc-side-card:hover {
        z-index: 40 !important;
        overflow: visible !important;
        box-shadow:
          0 24px 50px rgba(0, 0, 0, 0.65),
          0 0 0 1px rgba(255, 255, 255, 0.2) !important;
      }
      .calc-side-card p {
        max-height: 0 !important;
        opacity: 0 !important;
        overflow: hidden !important;
        transition:
          max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          opacity 0.3s ease,
          margin-top 0.3s ease !important;
        margin-top: 0 !important;
      }
      .calc-side-card:hover p {
        max-height: 400px !important;
        opacity: 1 !important;
        overflow: visible !important;
        margin-top: 8px !important;
      }

      /* === SLIDE 19: TOP 3 CARDS HALF HEIGHT BEFORE HOVER === */
      .s20-top-cards {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 20px !important;
        align-items: flex-start !important;
      }
      .s20-top-cards .glass-card {
        height: 125px !important;
        min-height: 125px !important;
        max-height: 125px !important;
        overflow: hidden !important;
        padding: 14px 18px !important;
        box-sizing: border-box !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        gap: 6px !important;
        transition:
          max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          height 0.45s ease,
          box-shadow 0.3s ease !important;
      }
      .s20-top-cards .glass-card:hover {
        height: auto !important;
        min-height: 250px !important;
        max-height: 580px !important;
        overflow: visible !important;
        z-index: 20 !important;
        box-shadow:
          0 24px 60px rgba(0, 0, 0, 0.8),
          0 0 0 1px rgba(255, 255, 255, 0.2) !important;
      }
      .s20-top-cards .glass-card h3 {
        font-size: 17px !important;
        font-weight: 900 !important;
        margin: 0 !important;
        line-height: 1.4 !important;
      }

      /* === SLIDE 5: BRAND TILE RIGHT-ALIGNED, LOGO ON RIGHT, CONTENT-FIT === */
      .brands-25-grid {
        display: grid !important;
        grid-template-columns: repeat(5, 1fr) !important;
        gap: 10px 12px !important;
      }
      .brand-tile {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding: 8px 12px !important;
        border-radius: 14px !important;
        gap: 10px !important;
        width: 100% !important;
        box-sizing: border-box !important;
        height: auto !important;
        min-height: 64px !important;
        text-align: right !important;
      }
      .brand-logo-slot {
        width: 44px !important;
        height: 44px !important;
        min-width: 44px !important;
        border-radius: 11px !important;
        background: #ffffff !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 4px !important;
        box-sizing: border-box !important;
        margin-bottom: 0 !important;
        flex-shrink: 0 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
      }
      .brand-tile-info {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        overflow: hidden !important;
        text-align: right !important;
        gap: 2px !important;
        flex: 1 !important;
      }
      .brand-tile-name {
        display: block !important;
        width: 100% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 13.5px !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-align: right !important;
        line-height: 1.35 !important;
        margin: 0 !important;
      }
      .brand-tile-cat {
        display: inline-block !important;
        max-width: 95% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 10.5px !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        background: rgba(255, 255, 255, 0.08) !important;
        padding: 1px 7px !important;
        border-radius: 6px !important;
        text-align: right !important;
        margin-top: 1px !important;
        line-height: 1.4 !important;
      }

      /* === SLIDE 8 ENHANCEMENTS: 2X HEIGHT, LARGER TYPOGRAPHY, LIVE PWA IFRAME === */
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-slide-grid {
        display: grid !important;
        grid-template-columns: 1.08fr 0.92fr !important;
        gap: 36px !important;
        align-items: center !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        gap: 18px !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card {
        padding: 24px 28px !important;
        border-radius: 20px !important;
        min-height: 140px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        gap: 8px !important;
        transition:
          transform 0.3s ease,
          box-shadow 0.3s ease !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card
        h3 {
        font-size: 24px !important;
        font-weight: 900 !important;
        margin: 0 !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card
        p {
        font-size: 14.5px !important;
        line-height: 1.8 !important;
        color: #e2e8f0 !important;
        margin-top: 6px !important;
        margin-bottom: 0 !important;
      }
      #balCard-welfare:hover {
        box-shadow: 0 16px 36px rgba(0, 147, 221, 0.45) !important;
        border-color: var(--sky-blue) !important;
        transform: translateY(-3px) !important;
      }
      #balCard-credit:hover {
        box-shadow: 0 16px 36px rgba(255, 119, 34, 0.45) !important;
        border-color: var(--persian-orange) !important;
        transform: translateY(-3px) !important;
      }
      #balCard-cash:hover {
        box-shadow: 0 16px 36px rgba(0, 212, 180, 0.45) !important;
        border-color: var(--persian-green) !important;
        transform: translateY(-3px) !important;
      }
      .iphone-dynamic-island {
        display: none !important;
      }
      @keyframes bounceDown {
        0%,
        100% {
          transform: translateY(0);
        }
        50% {
          transform: translateY(5px);
        }
      }
      .flow-pulse-arrow {
        animation: bounceDown 1.6s infinite ease-in-out;
      }

      /* === SLIDE 17: 2X FONT SIZE FOR ALLOCATION CARDS BEFORE HOVER === */
      .slide[data-title='مدل‌های ارائه اوورشارژ رفاهیات سازمانی']
        .glass-card
        h3,
      .slide[data-title='مدل‌های ارائه اوورشارژ رفاهیات سازمانی']
        .glass-card
        [style*='font-size:26px'] {
        font-size: 26px !important;
        font-weight: 900 !important;
      }
      .slide[data-title='مدل‌های ارائه اوورشارژ رفاهیات سازمانی']
        .glass-card
        p {
        font-size: 18px !important;
        line-height: 1.85 !important;
        color: #e2e8f0 !important;
      }

      /* === SLIDE 19: TOP 3 CARDS HALF HEIGHT BEFORE HOVER === */
      .s20-top-cards {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 20px !important;
        align-items: flex-start !important;
      }
      .s20-top-cards .glass-card,
      .s20-top-cards .s20-value-card {
        height: 125px !important;
        min-height: 125px !important;
        max-height: 125px !important;
        overflow: hidden !important;
        padding: 14px 18px !important;
        box-sizing: border-box !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        gap: 6px !important;
        transition:
          max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),
          height 0.45s ease,
          box-shadow 0.3s ease !important;
      }
      .s20-top-cards .glass-card:hover,
      .s20-top-cards .s20-value-card:hover {
        height: auto !important;
        min-height: 260px !important;
        max-height: 600px !important;
        overflow: visible !important;
        z-index: 25 !important;
        box-shadow:
          0 24px 60px rgba(0, 0, 0, 0.85),
          0 0 0 1px rgba(255, 255, 255, 0.2) !important;
      }

      /* === PER-CARD EXACT HOVER SHADOW COLORS (SCREENSHOTS 1 & 2) === */
      .glass-card[style*='var(--supernova)']:hover,
      .glass-card[style*='#FFDB04']:hover,
      .glass-card[style*='#FFD54F']:hover,
      .why-pillar-card[style*='var(--supernova)']:hover {
        box-shadow: 0 20px 48px rgba(255, 219, 4, 0.45) !important;
        border-color: var(--supernova) !important;
      }
      .glass-card[style*='var(--pastel-green)']:hover,
      .why-pillar-card[style*='var(--pastel-green)']:hover {
        box-shadow: 0 20px 48px rgba(0, 212, 180, 0.45) !important;
        border-color: var(--pastel-green) !important;
      }
      .glass-card[style*='var(--persian-orange)']:hover,
      .why-pillar-card[style*='var(--persian-orange)']:hover {
        box-shadow: 0 20px 48px rgba(255, 119, 34, 0.45) !important;
        border-color: var(--persian-orange) !important;
      }
      .glass-card[style*='var(--sky-blue)']:hover,
      .why-pillar-card[style*='var(--sky-blue)']:hover {
        box-shadow: 0 20px 48px rgba(0, 147, 221, 0.45) !important;
        border-color: var(--sky-blue) !important;
      }
      .glass-card[style*='var(--persian-green)']:hover,
      .why-pillar-card[style*='var(--persian-green)']:hover {
        box-shadow: 0 20px 48px rgba(0, 212, 180, 0.45) !important;
        border-color: var(--persian-green) !important;
      }
      .glass-card[style*='#A78BFA']:hover,
      .why-pillar-card[style*='#A78BFA']:hover {
        box-shadow: 0 20px 48px rgba(167, 139, 250, 0.45) !important;
        border-color: #a78bfa !important;
      }

      /* .glass-card .why-pillar-card[style*='border-top: 4px solid #a78bfa'] :hover {
        box-shadow: 0 20px 48px rgba(167, 139, 250, 0.45) !important;
        border-color: #a78bfa !important;
      } */
      
      .glass-card[style*='var(--persian-rose)']:hover,
      .glass-card[style*='#F16273']:hover,
      .glass-card[style*='border-right: 5px solid var(--persian-rose)']:hover {
        box-shadow: 0 20px 48px rgba(241, 98, 115, 0.45)  !important;
        border-color: var(--persian-rose) !important;
      }

      /* rgba(241, 98, 115, 0.45) */

      /* Slide 8: 0.5X height for 3 balance cards */
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col {
        gap: 10px !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card {
        padding: 12px 20px !important;
        border-radius: 16px !important;
        min-height: 70px !important;
        gap: 6px !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card
        h3 {
        font-size: 20px !important;
        font-weight: 900 !important;
        margin: 0 !important;
      }
      .slide[data-title='دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی']
        .demo-left-col
        .glass-card
        p {
        font-size: 13px !important;
        line-height: 1.6 !important;
        color: #cbd5e1 !important;
        margin: 4px 0 0 0 !important;
      }

      /* Slide 19: Equal spacing between top cards and bottom card & larger titles */
      .s20-top-cards {
        gap: 20px !important;
        /* margin-bottom: 20px !important; */
      }
      .s20-top-cards .glass-card h3,
      .s20-top-cards .s20-value-card h3 {
        font-size: 27px !important;
        font-weight: 900 !important;
        line-height: 1.35 !important;
      }
      /* .ux-flow-card {
        margin-top: 20px !important;
      } */
    </style>
  </head>
  <body>
    <svg
      style="position: absolute; width: 0; height: 0; overflow: hidden"
      aria-hidden="true">
      <defs>
        <symbol id="i-chart" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M4 20V12M12 20V6M20 20v-9" />
          </g>
        </symbol>
        <symbol id="i-wallet" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="3" y="7" width="18" height="13" rx="2" />
            <path d="M3 11h18" />
            <circle
              cx="16.5"
              cy="14.5"
              r="1"
              fill="currentColor"
              stroke="none" />
          </g>
        </symbol>
        <symbol id="i-swap" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M20 7H7l3-3M4 17h13l-3 3" />
          </g>
        </symbol>
        <symbol id="i-card" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="2.5" y="5.5" width="19" height="13" rx="2" />
            <path d="M2.5 10h19" />
          </g>
        </symbol>
        <symbol id="i-gift" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="3.5" y="9.5" width="17" height="10.5" rx="1" />
            <path d="M3.5 9.5h17M12 9.5V20" />
            <path d="M12 9.5C10 6 6.5 6 6.5 8.2 6.5 9.5 8 9.5 12 9.5Z" />
            <path d="M12 9.5c2-3.5 5.5-3.5 5.5-1.3 0 1.3-1.5 1.3-5.5 1.3Z" />
          </g>
        </symbol>
        <symbol id="i-send" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M21 3 3 10.5l7 2.5 2 7L21 3Z" />
          </g>
        </symbol>
        <symbol id="i-bolt" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z" />
          </g>
        </symbol>
        <symbol id="i-store" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M3 9h18l-1.5-5h-15L3 9Z" />
            <path d="M4 9v11h16V9" />
            <path d="M9.5 20v-6h5v6" />
          </g>
        </symbol>
        <symbol id="i-repeat" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M4 12a8 8 0 0 1 14-5l2-2M20 12a8 8 0 0 1-14 5l-2 2" />
          </g>
        </symbol>
        <symbol id="i-sliders" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h13M20 18h0" />
            <circle cx="16" cy="6" r="2" fill="currentColor" stroke="none" />
            <circle cx="9" cy="12" r="2" fill="currentColor" stroke="none" />
            <circle cx="16" cy="18" r="2" fill="currentColor" stroke="none" />
          </g>
        </symbol>
        <symbol id="i-eye" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7-10-7-10-7Z" />
            <circle cx="12" cy="12" r="3" />
          </g>
        </symbol>
        <symbol id="i-tag" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M12 2 21 11l-9.5 9.5a2 2 0 0 1-2.8 0L2 14V5a3 3 0 0 1 3-3h7Z" />
            <circle cx="8" cy="8" r="1.4" fill="currentColor" stroke="none" />
          </g>
        </symbol>
        <symbol id="i-layers" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="m12 3 9 5-9 5-9-5 9-5Z" />
            <path d="m3 13 9 5 9-5" />
          </g>
        </symbol>
        <symbol id="i-percent" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M5 19 19 5" />
            <circle cx="7" cy="7" r="2.3" />
            <circle cx="17" cy="17" r="2.3" />
          </g>
        </symbol>
        <symbol id="i-shirt" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M8 4 4 8l3 3 2-1.5V20h6V9.5L17 11l3-3-4-4-2 2h-4L8 4Z" />
          </g>
        </symbol>
        <symbol id="i-cart" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M3 4h2l2.4 12.2a2 2 0 0 0 2 1.6h7.2a2 2 0 0 0 2-1.6L20 8H6" />
            <circle
              cx="9.5"
              cy="21"
              r="1.2"
              fill="currentColor"
              stroke="none" />
            <circle cx="17" cy="21" r="1.2" fill="currentColor" stroke="none" />
          </g>
        </symbol>
        <symbol id="i-plane" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M21 12 3 5l3 7-3 7 18-7Z" />
          </g>
        </symbol>
        <symbol id="i-book" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M4 5.5C6 4.5 9 4.5 12 6c3-1.5 6-1.5 8-.5v13c-2-1-5-1-8 .5-3-1.5-6-1.5-8-.5v-13Z" />
            <path d="M12 6v13" />
          </g>
        </symbol>
        <symbol id="i-utensils" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M7 2v8M5 2v5a2 2 0 0 0 4 0V2M7 10v12M17 2c-2 0-3 2-3 5s1 4 3 4 3-1 3-4-1-5-3-5Zm0 9v11" />
          </g>
        </symbol>
        <symbol id="i-plus" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M12 5v14M5 12h14" />
          </g>
        </symbol>
        <symbol id="i-nocard" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="6" y="2" width="12" height="20" rx="2" />
            <path d="M11 18h2M3 3l18 18" />
          </g>
        </symbol>
        <symbol id="i-filecheck" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6Z" />
            <path d="M14 2v6h6M9 14l2 2 4-4" />
          </g>
        </symbol>
        <symbol id="i-network" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <circle cx="12" cy="4" r="2" />
            <circle cx="5" cy="18" r="2" />
            <circle cx="19" cy="18" r="2" />
            <path d="M12 6v6M12 12 5 16M12 12l7 4" />
          </g>
        </symbol>
        <symbol id="i-headset" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M4 13v-1a8 8 0 0 1 16 0v1" />
            <rect x="2.5" y="13" width="4" height="6" rx="1.5" />
            <rect x="17.5" y="13" width="4" height="6" rx="1.5" />
            <path d="M19.5 19v.5a3 3 0 0 1-3 3H13" />
          </g>
        </symbol>
        <symbol id="i-usercog" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <circle cx="9" cy="7" r="3.2" />
            <path d="M3 20c0-3.6 2.8-6 6-6 1 0 2 .2 2.8.6" />
            <circle cx="18" cy="16" r="2.2" />
            <path
              d="M18 12.7v1M18 18.3v1M21.3 16h-1M15.7 16h-1M20.1 13.9l-.7.7M16.6 17.4l-.7.7M20.1 18.1l-.7-.7M16.6 14.6l-.7-.7" />
          </g>
        </symbol>
        <symbol id="i-link" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M9 15 15 9M10 6l1-1a4 4 0 0 1 6 6l-1 1M14 18l-1 1a4 4 0 0 1-6-6l1-1" />
          </g>
        </symbol>
        <symbol id="i-activity" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M22 12h-4l-3 8-6-16-3 8H2" />
          </g>
        </symbol>
        <symbol id="i-chevron" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2.4"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="m15 6-6 6 6 6" />
          </g>
        </symbol>
        <symbol id="i-shield" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M12 2 4 5v6c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V5l-8-3Z" />
          </g>
        </symbol>
        <symbol id="i-ewanomark" viewBox="0 0 40 40">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2.6"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M11 9 L17 26 M21 7 L17 26 M17 26 L29 22" />
          </g>
          <circle cx="31.5" cy="23.2" r="1.7" fill="currentColor" />
          <circle cx="34.5" cy="19.4" r="1.7" fill="currentColor" />
        </symbol>
        <symbol id="i-chat" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M4 12c0-4.4 3.6-8 8-8s8 3.6 8 8-3.6 8-8 8c-1.2 0-2.4-.3-3.4-.7L4 20l1.2-4.3C4.4 14.6 4 13.3 4 12Z" />
          </g>
          <circle cx="9" cy="12" r="1.1" fill="currentColor" />
          <circle cx="12" cy="12" r="1.1" fill="currentColor" />
          <circle cx="15" cy="12" r="1.1" fill="currentColor" />
        </symbol>
        <symbol id="i-arrowup" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2.4"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M12 19V5M6 11l6-6 6 6" />
          </g>
        </symbol>
        <symbol id="i-arrowdown" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2.4"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M12 5v14M6 13l6 6 6-6" />
          </g>
        </symbol>
        <symbol id="i-bank" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M3 10 12 4l9 6" />
            <path d="M4 10h16v2H4zM5 12v8M9 12v8M15 12v8M19 12v8M3 21h18" />
          </g>
        </symbol>
        <symbol id="i-phone" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="7" y="2" width="10" height="20" rx="2" />
            <path d="M11 18h2" />
          </g>
        </symbol>
        <symbol id="i-home" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="m3 11 9-7 9 7" />
            <path d="M5 10v10h14V10" />
            <path d="M10 20v-6h4v6" />
          </g>
        </symbol>
        <symbol id="i-qr" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="3" y="3" width="7" height="7" rx="1" />
            <rect x="14" y="3" width="7" height="7" rx="1" />
            <rect x="3" y="14" width="7" height="7" rx="1" />
            <path d="M14 14h3v3h-3zM20 14v3M14 20h3M20 20v.01" />
          </g>
        </symbol>
        <symbol id="i-user" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <circle cx="12" cy="8" r="4" />
            <path d="M4 20c0-4.4 3.6-7 8-7s8 2.6 8 7" />
          </g>
        </symbol>
        <symbol id="i-search" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <circle cx="11" cy="11" r="7" />
            <path d="m21 21-4.3-4.3" />
          </g>
        </symbol>
        <symbol id="i-star" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2l-5-4.9 6.9-1z" />
          </g>
        </symbol>
        <symbol id="i-bell" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M6 9a6 6 0 0 1 12 0c0 4.5 1.5 6 1.5 6h-15S6 13.5 6 9Z" />
            <path d="M10 20a2 2 0 0 0 4 0" />
          </g>
        </symbol>
        <symbol id="i-car" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M4 16V11l2-5h12l2 5v5" />
            <path d="M4 16h16M6 16v2M18 16v2" />
            <circle
              cx="7.5"
              cy="16"
              r="1.3"
              fill="currentColor"
              stroke="none" />
            <circle
              cx="16.5"
              cy="16"
              r="1.3"
              fill="currentColor"
              stroke="none" />
          </g>
        </symbol>
        <symbol id="i-home2" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="4" y="4" width="16" height="16" rx="2" />
            <path d="M9 9h2M9 13h6M9 17h6" />
          </g>
        </symbol>
        <symbol id="i-building" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="4" y="3" width="16" height="18" rx="1" />
            <path d="M9 8h1M14 8h1M9 12h1M14 12h1M9 16h1M14 16h1" />
          </g>
        </symbol>
        <symbol id="i-pin" viewBox="0 0 24 24">
          <path
            fill="currentColor"
            d="M12 2C8.1 2 5 5.1 5 9c0 5.3 7 13 7 13s7-7.7 7-13c0-3.9-3.1-7-7-7Zm0 9.6a2.6 2.6 0 1 1 0-5.2 2.6 2.6 0 0 1 0 5.2Z" />
        </symbol>
        <symbol id="i-scanframe" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M4 8V5a1 1 0 0 1 1-1h3M20 8V5a1 1 0 0 0-1-1h-3M4 16v3a1 1 0 0 0 1 1h3M20 16v3a1 1 0 0 1-1 1h-3" />
          </g>
        </symbol>
        <symbol id="i-laptop" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="4" y="5" width="16" height="10" rx="1.2" />
            <path d="M2 19h20" />
          </g>
        </symbol>
        <symbol id="i-diamond" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M4 9h16L12 21 4 9Z" />
            <path d="m8 4-4 5h16l-4-5H8Z" />
          </g>
        </symbol>
        <symbol id="i-bottle" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <rect x="8" y="9" width="8" height="12" rx="1.5" />
            <path d="M10 9V5.5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1V9M9 4h6" />
          </g>
        </symbol>
        <symbol id="i-wrench" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M14.7 6.3a4 4 0 0 0-5.4 5l-6 6 2.4 2.4 6-6a4 4 0 0 0 5-5.4l-2.6 2.6-2-2 2.6-2.6Z" />
          </g>
        </symbol>
        <symbol id="i-chess" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <circle cx="12" cy="6" r="2.3" />
            <path
              d="M9.5 11c0 1.5 1 2 1 3.5S9 17 9 17h6s-1.5-1-1.5-2.5 1-2 1-3.5a2.5 2.5 0 0 0-5 0Z" />
            <path d="M7.5 20.5h9M8 17h8l.7 3.5H7.3L8 17Z" />
          </g>
        </symbol>
        <symbol id="i-backpack" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path d="M7 9V6a5 5 0 0 1 10 0v3" />
            <rect x="5" y="9" width="14" height="12" rx="2.5" />
            <path d="M9 13h6M9 21v-4h6v4" />
          </g>
        </symbol>
        <symbol id="i-bed" viewBox="0 0 24 24">
          <g
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round">
            <path
              d="M3 18v-6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v6M3 18v2M21 18v2M3 14h18" />
            <path d="M6 10V7a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v3" />
          </g>
        </symbol>
      </defs>
    </svg>

    <!-- AMBIENT ANIMATED CANVAS -->
    <div class="ambient-canvas">
      <div class="ambient-grid"></div>
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
      <div class="orb orb-3"></div>
    </div>

    <!-- =======================================================================
       PERSISTENT TOP BAR
       ======================================================================= -->
    <header class="deck-header">
      <div
        class="brand-cluster"
        style="display: flex; align-items: center; gap: 20px">
        <!-- Ewano Logo Badge -->
        <div
          class="header-ewano-logo"
          onclick="goToSlide(0)"
          title="اوانو"
          style="cursor: pointer; display: flex; align-items: center">
          <img
            src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..."
            alt="Ewano"
            style="
              height: 44px;
              width: auto;
              border-radius: 10px;
              display: block;
            " />
        </div>

        <!-- Partner Logos: EBCOM then MCI (RTL: EBCOM on right, MCI on left) -->
        <div
          class="header-partner-logos"
          style="
            display: flex;
            align-items: center;
            gap: 16px;
            padding-right: 16px;
            border-right: 1px solid rgba(255, 255, 255, 0.15);
          ">
          <img
            src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..."
            alt="EBCOM"
            style="
              height: 28px;
              width: auto;
              display: block;
              filter: brightness(1.1);
            "
            title="EBCOM" />
          <span
            style="
              display: inline-block;
              width: 1px;
              height: 24px;
              background: rgba(255, 255, 255, 0.18);
            "></span>
          <img
            src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..."
            alt="MCI"
            style="height: 28px; width: auto; display: block"
            title="همراه اول" />
        </div>
      </div>

      <!-- Chapter Quick Switcher -->
      <nav class="chapter-nav" id="chapterNav">
        <button class="chapter-btn active" onclick="goToSlide(0)">
          ۱. اکوسیستم و اوانو
        </button>
        <button class="chapter-btn" onclick="goToSlide(5)">
          ۲. دمو و ماشین‌حساب
        </button>
        <button class="chapter-btn" onclick="goToSlide(10)">
          ۳. مسیر ۶ مرحله‌ای اعتبار
        </button>
        <button class="chapter-btn" onclick="goToSlide(16)">
          ۴. رفاهیات و راهکار نقدی
        </button>
        <button class="chapter-btn" onclick="goToSlide(20)">
          ۵. شبکه پذیرندگی و آمار
        </button>
      </nav>

      <div class="header-actions">
        <button class="icon-btn" onclick="toggleDrawer()">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2.2">
            <line x1="3" y1="6" x2="21" y2="6" />
            <line x1="3" y1="12" x2="21" y2="12" />
            <line x1="3" y1="18" x2="21" y2="18" />
          </svg>
          <span>فهرست اسلایدها (۲۲)</span>
        </button>
        <button
          class="icon-btn"
          onclick="toggleFullScreen()"
          title="نمایش تمام‌صفحه (کلید F)">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2.2">
            <path
              d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3" />
          </svg>
          <span>تمام‌صفحه</span>
        </button>
      </div>
    </header>

    <!-- =======================================================================
       SLIDES STAGE (20 INTERACTIVE PRESENTATIONAL SLIDES)
       ======================================================================= -->
    <main class="stage-container" id="stageContainer">
      <!-- =====================================================================
         SLIDE 1: HERO COVER (Inspired by Figma Hero + Brand Book)
         ===================================================================== -->
      <section
        class="slide active"
        data-chapter="0"
        data-title="صفحه عنوان: راهکارهای سازمانی و اعتباری اوانو">
        <div class="slide-inner">
          <div class="grid-2-asym">
            <div style="display: flex; flex-direction: column; gap: 20px">
              <div
                class="anim-up delay-1"
                style="
                  display: flex;
                  align-items: center;
                  gap: 10px;
                  flex-wrap: wrap;
                ">
                <span class="eyebrow-badge"
                  >ارائه حضوری راهکارهای سازمانی B2B</span
                >
                <span class="eyebrow-badge orange"
                  >ویژه مدیران ارشد، منابع انسانی و مالی</span
                >
              </div>

              <h1
                class="slide-headline anim-up delay-2"
                style="font-size: clamp(30px, 3.2vw, 46px)">
                اعتبار و خدمات رفاهی کارکنان،<br />
                <span class="accent-green">متناسب با نیاز سازمان شما</span>
              </h1>

              <p class="slide-subtitle anim-up delay-3">
                با راهکارهای سازمانی <strong>اوانو</strong> و زیرساخت مالی
                <strong>EBCOM</strong>، مجموعه‌ای یکپارچه از خدمات اعتباری،
                رفاهی و نقدی را در اختیار کارکنان خود قرار دهید و مدیریت مزایای
                سازمانی را ساده، شفاف و هوشمند پیش ببرید.
              </p>

              <!-- Key Hero Stats Strip -->
              <div class="grid-3 anim-up delay-4" style="margin-top: 6px">
                <div
                  class="glass-card"
                  style="
                    padding: 16px 18px;
                    border-right: 4px solid var(--persian-green);
                  ">
                  <div
                    style="
                      font-size: 26px;
                      font-weight: 900;
                      color: var(--persian-green);
                    ">
                    +۲۸ میلیون
                  </div>
                  <p style="font-size: 12px; color: #e2e8f0; font-weight: 700">
                    کاربر فعال در اکوسیستم اوانو
                  </p>
                </div>
                <div
                  class="glass-card"
                  style="
                    padding: 16px 18px;
                    border-right: 4px solid var(--persian-orange);
                  ">
                  <div
                    style="
                      font-size: 26px;
                      font-weight: 900;
                      color: var(--persian-orange);
                    ">
                    ۹٬۴۱۵ مرچنت
                  </div>
                  <p style="font-size: 12px; color: #e2e8f0; font-weight: 700">
                    ۱۰٬۴۷۲ نقطه و شعبه پذیرندگی
                  </p>
                </div>
                <div
                  class="glass-card"
                  style="
                    padding: 16px 18px;
                    border-right: 4px solid var(--sky-blue);
                  ">
                  <div
                    style="
                      font-size: 26px;
                      font-weight: 900;
                      color: var(--sky-blue);
                    ">
                    +۲۰ همت
                  </div>
                  <p style="font-size: 12px; color: #e2e8f0; font-weight: 700">
                    حجم خرید و ۱۵ میلیون تراکنش ماهانه
                  </p>
                </div>
              </div>

              <div
                class="anim-up delay-5"
                style="
                  display: flex;
                  align-items: center;
                  gap: 14px;
                  margin-top: 6px;
                ">
                <button
                  class="nav-arrow-btn"
                  style="
                    background: var(--persian-green);
                    color: #0b0f13;
                    height: 46px;
                    padding: 0 26px;
                    font-size: 14px;
                  "
                  onclick="nextSlide()">
                  <span>شروع پرزنتیشن</span>
                  <svg
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2.5">
                    <line x1="19" y1="12" x2="5" y2="12" />
                    <polyline points="12 19 5 12 12 5" />
                  </svg>
                </button>
                <button
                  class="nav-arrow-btn"
                  style="height: 46px"
                  onclick="goToSlide(10)">
                  <span>مشاهده مسیر ۶ مرحله‌ای اعتبار</span>
                </button>
              </div>
            </div>

            <!-- Figma Hero Inspired 3D Floating Wallet Cards (3 Original + 4th Black Ewano Debit Card) -->
            <div class="hero-cards-stage anim-up delay-3">
              <!-- Card 1: Welfare (Blue) -->
              <div class="ewano-3d-card card-welfare">
                <div class="card-top-row">
                  <div class="card-chip"></div>
                  <span
                    style="
                      font-size: 10.5px;
                      font-weight: 800;
                      background: rgba(0, 0, 0, 0.22);
                      padding: 4px 10px;
                      border-radius: 99px;
                    "
                    >WELFARE BALANCE</span
                  >
                </div>
                <div>
                  <div class="card-balance-title">موجودی رفاهی سازمانی</div>
                  <div class="card-balance-sub">
                    تخصیص مزایا در سرفصل‌های معیشتی، سفر و بیمه
                  </div>
                </div>
                <div
                  style="
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-size: 11.5px;
                    font-weight: 800;
                  ">
                  <span>شارژ تشویقی تا ۶٪</span>
                  <span>ewano.app</span>
                </div>
              </div>

              <!-- Card 2: Credit (Orange) -->
              <div class="ewano-3d-card card-credit">
                <div class="card-top-row">
                  <div class="card-chip"></div>
                  <span
                    style="
                      font-size: 10.5px;
                      font-weight: 800;
                      background: rgba(0, 0, 0, 0.22);
                      padding: 4px 10px;
                      border-radius: 99px;
                    "
                    >CORPORATE CREDIT</span
                  >
                </div>
                <div>
                  <div class="card-balance-title">موجودی اعتبار اوانو</div>
                  <div class="card-balance-sub">
                    خرید اقساطی ۴ تا ۲۴ ماهه با ضمانت کسر از حقوق (ریوالوینگ)
                  </div>
                </div>
                <div
                  style="
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-size: 11.5px;
                    font-weight: 800;
                  ">
                  <span>بدون اعتبارسنجی بانکی</span>
                  <span>EBCOM</span>
                </div>
              </div>

              <!-- Card 3: Cash (Green) -->
              <div class="ewano-3d-card card-cash">
                <div class="card-top-row">
                  <div class="card-chip"></div>
                  <span
                    style="
                      font-size: 10.5px;
                      font-weight: 800;
                      background: rgba(0, 0, 0, 0.22);
                      padding: 4px 10px;
                      border-radius: 99px;
                    "
                    >CASH & GIFT CARD</span
                  >
                </div>
                <div>
                  <div class="card-balance-title">موجودی نقدی و گیفت‌کارت</div>
                  <div class="card-balance-sub">
                    شارژ مستقیم کیف پول نقدی و ووچرکارت‌های سازمانی
                  </div>
                </div>
                <div
                  style="
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-size: 11.5px;
                    font-weight: 800;
                  ">
                  <span>کارت به کارت و پرداخت آنی</span>
                  <span>EWANO WALLET</span>
                </div>
              </div>

              <!-- Card 4: Black Ewano Bank Debit Card (کلیک برای چرخش و مشاهده پشت کارت) -->
              <div
                class="ewano-3d-card card-debit-black"
                id="debitCardFlipper"
                onclick="toggleDebitCardFlip(this)"
                title="برای مشاهده پشت کارت کلیک کنید"
                style="cursor: pointer">
                <div class="debit-flipper-inner">
                  <!-- Front Side -->
                  <div class="debit-side debit-front">
                    <img
                      src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..."
                      alt="روی دبیت کارت اوانو"
                      style="
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                        display: block;
                        border-radius: 22px;
                      " />
                  </div>
                  <!-- Back Side -->
                  <div class="debit-side debit-back">
                    <img
                      src="data:...(base64 حذف شد برای صرفه‌جویی توکن)..."
                      alt="پشت دبیت کارت اوانو"
                      style="
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                        display: block;
                        border-radius: 22px;
                      " />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- =====================================================================
         SLIDE 2: MCI ECOSYSTEM (اکوسیستم همراه اول)
         ===================================================================== -->
      <section
        class="slide"
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
            اکوسیستم <span class="accent-green">همراه اول</span>؛ بزرگ‌ترین
            اپراتور ارتباطی و دیجیتال کشور
          </h2>
          <p class="slide-subtitle anim-up delay-2">
            همراه اول با تکیه بر مجموعه‌ای از شرکت‌ها و کسب‌وکارهای تخصصی،
            زنجیره
```
