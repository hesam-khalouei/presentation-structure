# Project Source Code (Part 6)

این فایل شامل کد پروژه است. هر فایل با `=== path ===` مشخص شده و کد داخل بلوک ```lang``` است. base64 فونت/تصویر حذف شده.

---

=== ./css/components.css ===

```css
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Components CSS (Refactored & Cleaned)
   ───────────────────────────────────────────────────────────────
   • Base Components (Buttons, Badges, Glass Cards)
   • Grid System (top-aligned)
   • Hero 3D Cards
   • Ecosystem & Services
   • Brands & Logos
   • Calculator
   • iPhone & PWA Demo
   • Voucher Cards (3D Flip)
   • Iran Map
   • Client Marquee
   • Deck Footer
   • Utility Classes
   ═══════════════════════════════════════════════════════════════ */

/* =========================================================================
   BASE COMPONENTS
   ========================================================================= */
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
  transition:
    border-color 0.2s ease,
    background 0.2s ease,
    color 0.2s ease;
}

.icon-btn:hover {
  border-color: var(--persian-green);
  background: var(--persian-green-soft);
  color: var(--persian-green);
}

.anim-up {
  opacity: 0;
  transform: translateY(22px);
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

/* ---------- Glass Card (پایه) ---------- */
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
  box-shadow: 0 14px 34px rgba(0, 0, 0, 0.28);

  /* ⚠️ مهم: فقط property های امن انیمیت می‌شن — نه transform */
  transition:
    border-color 0.3s ease,
    box-shadow 0.3s ease,
    background 0.3s ease;

  /* ⚠️ مهم: مبدأ انیمیشن از بالا */
  transform-origin: top center;

  /* ⚠️ مهم: کارت‌ها در گرید از بالا تراز می‌شن */
  align-self: start;
}

.glass-card:hover {
  border-color: var(--border-green);
  box-shadow: 0 18px 42px rgba(0, 212, 180, 0.14);
}

.glass-card.orange-hover:hover {
  border-color: rgba(255, 119, 34, 0.5);
  box-shadow: 0 18px 42px rgba(255, 119, 34, 0.15);
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
  transition:
    background 0.2s ease,
    color 0.2s ease,
    border-color 0.2s ease,
    box-shadow 0.2s ease;
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

.svg-flow-line {
  stroke-dasharray: 6 6;
  animation: dashFlow 1.6s linear infinite;
}

.svg-pulse {
  transform-origin: center;
  animation: pulseRing 3s ease-in-out infinite;
}

/* =========================================================================
   GRID SYSTEM (همه از بالا تراز)
   ========================================================================= */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  align-items: start;
}
.grid-2-asym {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 28px;
  align-items: start;
}
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  align-items: start;
}
.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  align-items: start;
}
.grid-5 {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
  align-items: start;
}
.services-10-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  align-items: start;
}
.companies-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  align-items: start;
}

/* =========================================================================
   HERO 3D CARDS (Slide 1)
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
    border-color 0.35s ease;
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

.ewano-3d-card.card-welfare {
  background: linear-gradient(135deg, #0093dd 0%, #00548a 100%);
  transform: translate3d(-115px, -105px, 10px) rotate(-9deg);
  z-index: 2;
}

.ewano-3d-card.card-credit {
  background: linear-gradient(135deg, #ff7722 0%, #c84b00 100%);
  transform: translate3d(-40px, -38px, 30px) rotate(-3deg);
  z-index: 3;
}

.ewano-3d-card.card-cash {
  background: linear-gradient(135deg, #00d4b4 0%, #008872 100%);
  transform: translate3d(35px, 30px, 50px) rotate(3deg);
  z-index: 4;
}

.ewano-3d-card.card-debit-black {
  background: linear-gradient(135deg, #2a2d32 0%, #121417 55%, #090a0c 100%);
  border: 1.5px solid rgba(255, 255, 255, 0.32);
  transform: translate3d(110px, 98px, 70px) rotate(9deg);
  z-index: 5;
  padding: 0;
}

.ewano-3d-card.card-debit-black::after {
  display: none;
}

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

/* Debit Card Flip */
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

/* =========================================================================
   ECOSYSTEM & SERVICES
   ========================================================================= */
.ecosystem-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 24px;
  align-items: start;
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
  transition:
    border-color 0.25s ease,
    background 0.25s ease,
    transform 0.25s ease;
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
.comp-name {
  font-weight: 800;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ---------- Service Tile ---------- */
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
  align-self: start;
  transform-origin: top center;
  transition:
    border-color 0.28s ease,
    background 0.28s ease,
    box-shadow 0.28s ease;
}

.service-tile:hover,
.service-tile.active {
  background: linear-gradient(
    180deg,
    rgba(0, 212, 180, 0.18) 0%,
    rgba(0, 212, 180, 0.04) 100%
  );
  border-color: var(--persian-green);
  box-shadow: 0 12px 26px rgba(0, 212, 180, 0.18);
}

.service-icon-box {
  width: 60px;
  height: 60px;
  border-radius: 18px;
  background: rgba(0, 212, 180, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--persian-green);
  transition:
    background 0.25s ease,
    color 0.25s ease,
    transform 0.25s ease;
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
   BRANDS & LOGOS
   ========================================================================= */
.brands-25-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  align-items: start;
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

.comp-logo-box,
.brand-logo-slot,
.pill-brand-logo,
.client-circle-logo,
.client-logo-box,
.logo-dot {
  background: #ffffff !important;
}

/* =========================================================================
   CALCULATOR (Slide 10)
   ========================================================================= */
.calc-grid-layout {
  display: grid;
  grid-template-columns: 1.18fr 0.82fr;
  gap: 24px;
  align-items: start;
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
  transition:
    border-color 0.22s ease,
    background 0.22s ease,
    transform 0.22s ease,
    box-shadow 0.22s ease;
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
.calc-side-card:hover p {
  max-height: 500px !important;
}

/* =========================================================================
   IPHONE & PWA DEMO (Slide 8)
   ========================================================================= */
.demo-slide-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 28px;
  align-items: start;
}
.demo-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 0;
}
.iphone-18-pro-max {
  width: 100% !important;
  max-width: 608px !important;
  height: 720px !important;
  aspect-ratio: 440 / 956;
  border-radius: 54px !important;
  padding: 12px !important;
  background: #000000;
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

/* =========================================================================
   VOUCHER CARDS (Slide 17 & 18)
   ========================================================================= */
.voucher-vertical-stage {
  position: relative;
  height: 420px;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1200px;
}
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

/* =========================================================================
   IRAN MAP (Slide 20)
   ========================================================================= */
.network-map-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 22px;
  align-items: start;
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
    fill 0.25s ease,
    opacity 0.25s ease,
    filter 0.25s ease;
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

/* =========================================================================
   LOGO DOTS & MARQUEE (Slides 5, 20, 21)
   ========================================================================= */
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
  transition:
    transform 0.25s ease,
    box-shadow 0.25s ease;
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

/* =========================================================================
   CLIENT MARQUEE (Slide 21)
   ========================================================================= */
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
    border-color 0.25s ease,
    box-shadow 0.25s ease;
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

/* =========================================================================
   WHY EWANO PILLARS (Slide 21)
   ========================================================================= */
.why-ewano-5grid {
  gap: 16px !important;
  align-items: start !important;
}
.why-pillar-card {
  padding: 22px 18px !important;
  text-align: center;
  min-height: 96px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
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
   WELFARE CATEGORIES (Slide 16)
   ========================================================================= */
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
  transition:
    background 0.25s ease,
    border-color 0.25s ease,
    color 0.25s ease,
    box-shadow 0.25s ease;
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

/* =========================================================================
   UX FLOW (Slide 19)
   ========================================================================= */
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

/* =========================================================================
   UTILITY CLASSES
   ========================================================================= */
.flex {
  display: flex;
}
.flex-col {
  display: flex;
  flex-direction: column;
}
.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
.flex-between {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.flex-start {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
.flex-gap-8 {
  gap: 8px;
}
.flex-gap-10 {
  gap: 10px;
}
.flex-gap-12 {
  gap: 12px;
}
.flex-gap-14 {
  gap: 14px;
}
.flex-gap-16 {
  gap: 16px;
}
.flex-gap-20 {
  gap: 20px;
}
.flex-wrap {
  flex-wrap: wrap;
}

.text-white {
  color: #ffffff;
}
.text-muted {
  color: #cbd5e1;
}
.text-green {
  color: var(--persian-green);
}
.text-orange {
  color: var(--persian-orange);
}
.text-sky {
  color: var(--sky-blue);
}
.text-purple {
  color: #a78bfa;
}
.font-bold {
  font-weight: 700;
}
.font-black {
  font-weight: 900;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.dir-ltr {
  direction: ltr;
}
.dir-rtl {
  direction: rtl;
}

.text-xs {
  font-size: 11.5px;
}
.text-sm {
  font-size: 13px;
}
.text-md {
  font-size: 14px;
}
.text-lg {
  font-size: 16px;
}
.text-xl {
  font-size: 18px;
}
.text-2xl {
  font-size: 22px;
}
.text-3xl {
  font-size: 26px;
}
.text-4xl {
  font-size: 32px;
}

.bg-glass {
  background: rgba(255, 255, 255, 0.04);
}
.border-glass {
  border: 1px solid var(--border-glass);
}
.border-top-green {
  border-top: 4px solid var(--persian-green);
}
.border-top-orange {
  border-top: 4px solid var(--persian-orange);
}
.border-top-sky {
  border-top: 4px solid var(--sky-blue);
}
.border-right-green {
  border-right: 5px solid var(--persian-green);
}
.border-right-orange {
  border-right: 5px solid var(--persian-orange);
}
.border-right-sky {
  border-right: 5px solid var(--sky-blue);
}
.border-right-purple {
  border-right: 5px solid #a78bfa;
}
.rounded-xl {
  border-radius: 16px;
}
.rounded-2xl {
  border-radius: 22px;
}
.rounded-pill {
  border-radius: 999px;
}

.p-2 {
  padding: 8px;
}
.p-3 {
  padding: 12px;
}
.p-4 {
  padding: 16px;
}
.p-5 {
  padding: 20px;
}
.p-6 {
  padding: 24px;
}
.px-4 {
  padding-left: 16px;
  padding-right: 16px;
}
.py-2 {
  padding-top: 8px;
  padding-bottom: 8px;
}
.py-4 {
  padding-top: 16px;
  padding-bottom: 16px;
}
.mt-1 {
  margin-top: 4px;
}
.mt-2 {
  margin-top: 8px;
}
.mt-4 {
  margin-top: 16px;
}
.mt-6 {
  margin-top: 24px;
}
.mb-1 {
  margin-bottom: 4px;
}
.mb-2 {
  margin-bottom: 8px;
}
.mb-4 {
  margin-bottom: 16px;
}
.w-full {
  width: 100%;
}
.h-full {
  height: 100%;
}

.icon-box-sm {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  flex-shrink: 0;
}
.icon-box-md {
  width: 54px;
  height: 54px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
}

/* =========================================================================
   HOVER-TO-EXPAND — فقط از پایین باز می‌شه
   ========================================================================= */

/* محتوای مخفی داخل کارت‌ها */
.glass-card:not(.no-collapse) p,
.glass-card:not(.no-collapse) ul,
.glass-card:not(.no-collapse) .hover-reveal,
.service-tile p {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  margin-top: 0 !important;
  margin-bottom: 0 !important;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
  border-top-color: transparent !important;
  transform: translateY(-8px);
  transition:
    max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),
    opacity 0.35s ease,
    transform 0.35s ease,
    margin 0.35s ease,
    padding 0.35s ease;
}

/* در هاور — بدون transform روی کارت (فقط border + shadow) */
.glass-card:not(.no-collapse):hover,
.glass-card:not(.no-collapse):focus-within,
.service-tile:hover,
.service-tile.active {
  transform: none !important;
  /* border-color: var(--persian-green) !important; */
  box-shadow: 0 20px 44px rgba(0, 212, 180, 0.18) !important;
  z-index: 15;
}

.glass-card.orange-hover:not(.no-collapse):hover {
  transform: none !important;
  border-color: var(--persian-orange) !important;
  box-shadow: 0 20px 44px rgba(255, 119, 34, 0.2) !important;
}

/* نمایش محتوا در هاور */
.glass-card:not(.no-collapse):hover p,
.glass-card:not(.no-collapse):hover ul,
.glass-card:not(.no-collapse):hover .hover-reveal,
.glass-card:not(.no-collapse):focus-within p,
.glass-card:not(.no-collapse):focus-within ul,
.glass-card:not(.no-collapse):focus-within .hover-reveal,
.service-tile:hover p,
.service-tile.active p {
  max-height: 480px;
  opacity: 1;
  transform: translateY(0);
  margin-top: 8px !important;
}

/* حذف کامل transform و ::after از glass-card */
.glass-card::after,
.glass-card:not(.no-collapse)::after {
  content: none !important;
  display: none !important;
}

/* اکسپند دستی */
.glass-card.expanded-box p,
.glass-card.expanded-box ul,
.glass-card.expanded-box .hover-reveal,
.service-tile.expanded-box p {
  max-height: 420px !important;
  opacity: 1 !important;
  transform: translateY(0) !important;
  margin-top: 8px !important;
}

/* =========================================================================
   DECK FOOTER (Sticky Bottom Bar)
   ========================================================================= */
.deck-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 90;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 10px 28px 12px;
  background: rgba(14, 19, 24, 0.82);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid var(--border-glass);
  box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.35);
  font-family: var(--font-main);
}

.deck-footer .progress-track {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: rgba(255, 255, 255, 0.06);
  overflow: hidden;
}

.deck-footer .progress-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(
    90deg,
    var(--persian-green),
    var(--persian-orange)
  );
  border-radius: 0 999px 999px 0;
  transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 0 12px var(--persian-green-glow);
}

.deck-footer .nav-controls {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-shrink: 0;
}

/* .deck-footer .slide-counter-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-glass);
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  white-space: nowrap;
} */

.deck-footer .slide-counter-pill {
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
  /* transition:
    background 0.2s ease,
    color 0.2s ease,
    border-color 0.2s ease,
    box-shadow 0.2s ease; */
}

.deck-footer .slide-counter-pill strong {
  font-weight: 900;
  font-size: 13.5px;
}

.deck-footer .slide-counter-pill #currentSlideNum {
  color: var(--persian-green);
}

.deck-footer .slide-counter-pill #totalSlideNum {
  color: #ffffff;
}

.deck-footer .slide-dots {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  flex: 1;
  flex-wrap: wrap;
  min-width: 0;
}

.deck-footer .slide-dots .dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  cursor: pointer;
  padding: 0;
  transition:
    background 0.25s ease,
    width 0.25s ease,
    box-shadow 0.25s ease;
}

.deck-footer .slide-dots .dot:hover {
  background: var(--persian-green);
}

.deck-footer .slide-dots .dot.active {
  background: var(--persian-green);
  width: 22px;
  border-radius: 999px;
  box-shadow: 0 0 10px var(--persian-green-glow);
}

.deck-footer .text-xs {
  flex-shrink: 0;
  white-space: nowrap;
  font-size: 11px;
}

.deck-footer kbd {
  font-family: var(--font-main);
  font-size: 10.5px;
  font-weight: 800;
  display: inline-block;
  min-width: 20px;
  text-align: center;
  border: 1px solid rgba(255, 255, 255, 0.15);
}
```

=== ./css/base.css ===

```css
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Main CSS
   ───────────────────────────────────────────────────────────────
   • Font Faces (IRANYekanX)
   • CSS Variables (:root)
   • Reset & Base
   • Ambient Background (Canvas, Orbs)
   • Keyframes (سراسری)
   ═══════════════════════════════════════════════════════════════ */

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
      src: local('IRANYekanXVF'), local('IRANYekanX'), local('IRANYekanX-UltraLight'), url('../assets/fonts/IRANYekanX-Light.woff') format('woff');
      font-weight: 100 300;
      font-style: normal;
      font-display: swap;
    }

@font-face {
      font-family: 'IRANYekanX';
      src: local('IRANYekanXVF'), local('IRANYekanX'), local('IRANYekanX-Regular'), local('IRANYekanX-Medium'), url('../assets/fonts/IRANYekanX-Regular.woff') format('woff');
      font-weight: 400 500;
      font-style: normal;
      font-display: swap;
    }

@font-face {
      font-family: 'IRANYekanX';
      src: local('IRANYekanXVF'), local('IRANYekanX'), local('IRANYekanX-Bold'), local('IRANYekanX-DemiBold'), local('IRANYekanX-ExtraBold'), local('IRANYekanX-Black'), url('../assets/fonts/IRANYekanX-Bold.woff') format('woff');
      font-weight: 600 900;
      font-style: normal;
      font-display: swap;
    }

:root {
      --persian-green: #00D4B4;
      --persian-green-dark: #00A68C;
      --persian-green-deep: #007A66;
      --persian-green-glow: rgba(0, 212, 180, 0.28);
      --persian-green-soft: rgba(0, 212, 180, 0.12);
      --pastel-green: #3DD598;

      --persian-orange: #FF7722;
      --persian-orange-dark: #E05A00;
      --persian-orange-glow: rgba(255, 119, 34, 0.28);
      --persian-orange-soft: rgba(255, 119, 34, 0.12);

      --supernova: #FFDB04;
      --royal-purple: #6F59A9;
      --persian-rose: #F16273;
      --sky-blue: #0093DD;

      --outer-space: #444444;
      --bg-dark: #0E1318;
      --bg-dark-card: #171F26;
      --bg-dark-elevated: #1F2933;
      --whiteout: #F9FBFC;
      --text-light: #F9FBFC;
      --text-muted: #94A3B8;
      --border-glass: rgba(255, 255, 255, 0.1);
      --border-green: rgba(0, 212, 180, 0.35);

      --font-main: 'IRANYekanX', 'Vazirmatn', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

* {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-font-smoothing: antialiased;
    }

html, body {
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
        radial-gradient(circle at 15% 18%, rgba(0, 212, 180, 0.13) 0%, transparent 42%),
        radial-gradient(circle at 85% 82%, rgba(255, 119, 34, 0.09) 0%, transparent 42%),
        radial-gradient(circle at 50% 50%, rgba(111, 89, 169, 0.06) 0%, transparent 60%),
        linear-gradient(135deg, #0B0F13 0%, #121820 50%, #0D1318 100%);
    }

.ambient-grid {
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(to right, rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255,255,255,0.025) 1px, transparent 1px);
      background-size: 48px 48px;
      mask-image: radial-gradient(circle at center, black 40%, transparent 90%);
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
      0% { transform: translate(0, 0) scale(1); }
      50% { transform: translate(-40px, 30px) scale(1.08); }
      100% { transform: translate(30px, -25px) scale(0.95); }
    }

@keyframes fadeUpIn {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

@keyframes floatCard1 {
      0% { transform: translate3d(-85px, -45px, 40px) rotate(-8deg); }
      100% { transform: translate3d(-95px, -58px, 50px) rotate(-5deg); }
    }

@keyframes floatCard2 {
      0% { transform: translate3d(10px, 15px, 60px) rotate(3deg); }
      100% { transform: translate3d(15px, 2px, 75px) rotate(6deg); }
    }

@keyframes floatCard3 {
      0% { transform: translate3d(100px, 75px, 20px) rotate(13deg); }
      100% { transform: translate3d(110px, 62px, 35px) rotate(10deg); }
    }

/* Pulse & SVG Motion Keyframes */
@keyframes pulseRing {
      0% { transform: scale(0.92); opacity: 0.8; }
      50% { transform: scale(1.08); opacity: 0.35; }
      100% { transform: scale(0.92); opacity: 0.8; }
    }

@keyframes dashFlow {
      to { stroke-dashoffset: -40; }
    }

/* =========================================================================
       REQUIREMENT 1: GLOBAL IRANYEKANX ENFORCEMENT
       ========================================================================= */
body, button, input, select, textarea, svg text, .phone-screen, .city-lbl, .city-n {
      font-family: 'IRANYekanX', 'Vazirmatn', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

@keyframes ph-tap { from { transform: scale(0.6); opacity: 1; } to { transform: scale(1.8); opacity: 0; } }

@keyframes qr-line { to { top: 92%; } }

@keyframes chat-dot { 50% { opacity: 0.3; transform: translateY(-2px); } }

@keyframes lm-slide { from { transform: translateX(0); } to { transform: translateX(50%); } }

@keyframes lm-slide-ltr {
      from { transform: translateX(50%); }
      to { transform: translateX(0); }
    }

@keyframes clientScrollRight {
      from { transform: translateX(50%); }
      to { transform: translateX(0); }
    }

@keyframes clientScrollLeft {
      from { transform: translateX(0); }
      to { transform: translateX(-50%); }
    }
.stage-container {
  position: relative;
  z-index: 1;
  width: 100vw;
  height: 100vh;
  padding-top: 88px;    /* ارتفاع هدر */
  padding-bottom: 88px; /* ارتفاع فوتر */
  overflow: hidden;
}
```

=== ./js/animations.js ===

```javascript
// فایل animations.js — فعلاً خالی. منطق در navigation.js است
```

=== ./js/main.js ===

```javascript
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Bootstrap & Initialization
   ───────────────────────────────────────────────────────────────
   • اطمینان از وجود اسلاید فعال
   • بررسی صحت توابع اصلی
   • مدیریت resize و visibility
   • منتظر لود شدن اسلایدها و کامپوننت‌ها می‌مونه
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ═══════════════════════════════════════════
  // ۱) تنظیمات
  // ═══════════════════════════════════════════
  const CONFIG = {
    DEBUG: false,
    REQUIRED_FNS: [
      'goToSlide',
      'nextSlide',
      'prevSlide',
      'toggleDrawer',
      'toggleFullScreen'
    ],
    REQUIRED_DOM: [
      '.stage-container',
      '.deck-header',
      '.deck-footer'
    ]
  };

  // ═══════════════════════════════════════════
  // ۲) Utilities
  // ═══════════════════════════════════════════
  const log = {
    info(msg) {
      if (CONFIG.DEBUG) {
        console.log(
          `%c[Ewano]%c ${msg}`,
          'background:#00D4B4;color:#0B0F13;padding:2px 6px;border-radius:4px;font-weight:bold;',
          'color:inherit;'
        );
      }
    },
    warn(msg) {
      if (CONFIG.DEBUG) console.warn(`[Ewano] ${msg}`);
    },
    error(msg) {
      console.error(`[Ewano] ${msg}`);
    },
    summary(count) {
      if (CONFIG.DEBUG) {
        console.log(
          `%c✅ Ewano B2B Presentation — ${count} slides`,
          'background:#00D4B4;color:#0B0F13;padding:4px 12px;border-radius:6px;font-weight:bold;font-size:13px;'
        );
      }
    }
  };

  function isFn(name) {
    return typeof window[name] === 'function';
  }

  function $(sel) {
    return document.querySelector(sel);
  }

  // ═══════════════════════════════════════════
  // ۳) Bootstrap Steps
  // ═══════════════════════════════════════════
  function ensureActiveSlide() {
    const slides = document.querySelectorAll('.slide');
    if (slides.length === 0) {
      return null;
    }
    if (!document.querySelector('.slide.active')) {
      slides[0].classList.add('active');
      log.info('اسلاید اول به عنوان active تنظیم شد');
    }
    return slides;
  }

  function checkRequiredFns() {
    const missing = CONFIG.REQUIRED_FNS.filter(fn => !isFn(fn));
    if (missing.length > 0) {
      missing.forEach(fn => log.warn(`تابع ${fn} پیدا نشد`));
    }
    return missing.length === 0;
  }

  function checkRequiredDOM() {
    const missing = CONFIG.REQUIRED_DOM.filter(sel => !$(sel));
    if (missing.length > 0) {
      missing.forEach(sel => log.warn(`عنصر ${sel} پیدا نشد`));
    }
    return missing.length === 0;
  }

  function setupResizeHandler() {
    let timer;
    window.addEventListener('resize', () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        log.info(`viewport: ${window.innerWidth}×${window.innerHeight}`);
      }, 200);
    });
  }

  function setupVisibilityHandler() {
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        log.info('صفحه مخفی شد — pause');
      } else {
        log.info('صفحه دوباره نمایان شد — resume');
      }
    });
  }

  function setupErrorBoundary() {
    window.addEventListener('error', (event) => {
      log.error(`خطای JS: ${event.message} در ${event.filename}:${event.lineno}`);
    });
    window.addEventListener('unhandledrejection', (event) => {
      log.error(`Promise rejection: ${event.reason}`);
    });
  }

  // ═══════════════════════════════════════════
  // ۴) Main Bootstrap
  // ═══════════════════════════════════════════
  function bootstrap() {
    log.info('شروع bootstrap...');

    if (!checkRequiredDOM()) {
      log.warn('برخی از عناصر DOM اصلی پیدا نشدن');
    }

    const slides = ensureActiveSlide();
    if (!slides) {
      log.error('هیچ اسلایدی پیدا نشد — bootstrap متوقف شد');
      return;
    }

    const fnsOk = checkRequiredFns();
    if (!fnsOk) {
      log.warn('برخی از توابع اصلی تعریف نشدن');
    }

    setupResizeHandler();
    setupVisibilityHandler();
    setupErrorBoundary();

    log.summary(slides.length);
    log.info('bootstrap کامل شد ✅');
  }

  // ═══════════════════════════════════════════
  // ۵) اجرا — منتظر اسلایدها می‌مونه
  // ═══════════════════════════════════════════
  let hasRun = false;

  function startBootstrap() {
    if (hasRun) return;
    hasRun = true;

    // اگه اسلایدها هنوز لود نشدن، صبر کن
    if (document.querySelectorAll('.slide').length === 0) {
      log.info('اسلایدها هنوز لود نشدن — منتظر slidesLoaded...');
      window.addEventListener('slidesLoaded', () => {
        log.info('slidesLoaded دریافت شد — اجرای bootstrap');
        bootstrap();
      }, { once: true });

      // fallback: بعد از ۵ ثانیه اگه هنوز خبری نشد
      setTimeout(() => {
        if (!hasRun) return;
        if (document.querySelectorAll('.slide').length === 0) {
          log.error('اسلایدها لود نشدن — bootstrap اجرا نمی‌شه');
        }
      }, 5000);
      return;
    }

    bootstrap();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startBootstrap);
  } else {
    startBootstrap();
  }
})();
```

=== ./js/demo.js ===

```javascript
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Interactive PWA Demo Engine
   ───────────────────────────────────────────────────────────────
   • Phone screen tabs (ph-home, ph-c2c, ...)
   • Back navigation
   • Tab click handlers
   ═══════════════════════════════════════════════════════════════ */

// REQUIREMENT 4: INTERACTIVE APP DEMO ENGINE (PWA + ewano-b2b-deck.html)
    // =========================================================================
    (function(){
      var demoTabs = document.querySelectorAll('.demo-tab');
      var prevScreen = 'ph-home';
      function showPhoneScreen(id){
        var cur = document.querySelector('.ph-screen.active');
        if (cur && cur.id !== id) prevScreen = cur.id;
        demoTabs.forEach(function(t){ t.classList.toggle('active', t.dataset.screen === id); });
        document.querySelectorAll('.ph-screen').forEach(function(s){ s.classList.toggle('active', s.id === id); });
      }
      window.showPhoneScreen = showPhoneScreen;
      window.phoneBack = function(){ showPhoneScreen(prevScreen); };
      demoTabs.forEach(function(tab){
        tab.addEventListener('click', function(){ showPhoneScreen(tab.dataset.screen); });
      });
      document.querySelectorAll('.ph-nav a[data-tab]').forEach(function(a){
        a.addEventListener('click', function(){ showPhoneScreen(a.dataset.tab); });
      });
    })();
```

=== ./js/navigation.js ===

```javascript
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Navigation & Slide Engine
   ───────────────────────────────────────────────────────────────
   • goToSlide / nextSlide / prevSlide
   • Chapter navigation
   • Keyboard controls (←/→/F/Esc/Space)
   • Slide dots + Drawer
   • Fullscreen
   • Card Flip handlers
   • Iran Map tooltip
   • Async-compatible (منتظر componentsLoaded و slidesLoaded)
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ═══════════════════════════════════════════
  // State
  // ═══════════════════════════════════════════
  let slides = [];
  let totalSlides = 0;
  let currentIndex = 0;

  // ═══════════════════════════════════════════
  // Utilities
  // ═══════════════════════════════════════════
  function toPersianDigits(num) {
    const farsiDigits = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'];
    return String(num).replace(/\d/g, x => farsiDigits[x]);
  }

  function $(sel) { return document.querySelector(sel); }
  function $$(sel) { return Array.from(document.querySelectorAll(sel)); }

  // ═══════════════════════════════════════════
  // Init Deck (فقط یه بار اجرا می‌شه)
  // ═══════════════════════════════════════════
  let deckInitialized = false;

  function initDeck() {
    if (deckInitialized) return;

    slides = $$('.slide');
    totalSlides = slides.length;

    if (totalSlides === 0) {
      console.warn('[Navigation] هنوز اسلایدی بارگذاری نشده.');
      return;
    }

    // چک می‌کنیم که Header و Footer هم لود شده باشن
    if (!$('#chapterNav') || !$('#slideDots')) {
      console.warn('[Navigation] Header یا Footer هنوز آماده نیست.');
      return;
    }

    console.log(`[Navigation] ${totalSlides} اسلاید آماده شد.`);

    // تنظیم total slide number
    const totalSlideNumEl = $('#totalSlideNum');
    if (totalSlideNumEl) totalSlideNumEl.textContent = toPersianDigits(totalSlides);

    // ساخت Dots
    const slideDotsContainer = $('#slideDots');
    if (slideDotsContainer) {
      slideDotsContainer.innerHTML = '';
      slides.forEach((slide, idx) => {
        const dot = document.createElement('div');
        // ۵ اسلاید وسط مسیر ۶ مرحله‌ای (indices 10-14) رنگ نارنجی می‌گیرن
        dot.className = 'slide-dot' + (idx >= 10 && idx <= 14 ? ' journey-dot' : '');
        dot.title = slide.getAttribute('data-title') || `اسلاید ${idx + 1}`;
        dot.onclick = () => goToSlide(idx);
        slideDotsContainer.appendChild(dot);
      });
    }

    // ساخت Drawer List
    const drawerList = $('#drawerList');
    if (drawerList) {
      drawerList.innerHTML = '';
      slides.forEach((slide, idx) => {
        const item = document.createElement('div');
        item.className = 'drawer-item';
        item.onclick = () => { goToSlide(idx); toggleDrawer(); };
        item.innerHTML = `
          <div class="drawer-item-num">${toPersianDigits(idx + 1)}</div>
          <div style="font-size:13px; font-weight:700; color:#E2E8F0;">
            ${slide.getAttribute('data-title') || 'اسلاید'}
          </div>
        `;
        drawerList.appendChild(item);
      });
    }

    // راه‌اندازی اولیه
    currentIndex = 0;
    updateDeckUI();
    deckInitialized = true;

    // فعال‌سازی نقشه (اگه وجود داشت)
    initMapTooltips();

    // فعال‌سازی کلیک روی کارت‌ها برای باز/بسته شدن (موبایل)
    setupCardExpand();
  }

  // ═══════════════════════════════════════════
  // Update UI (بعد از هر تغییر)
  // ═══════════════════════════════════════════
  function updateDeckUI() {
    if (!slides.length) return;

    // اسلاید فعال
    slides.forEach((slide, idx) => {
      slide.classList.toggle('active', idx === currentIndex);
    });

    // شمارنده
    const currentSlideNumEl = $('#currentSlideNum');
    if (currentSlideNumEl) currentSlideNumEl.textContent = toPersianDigits(currentIndex + 1);

    // نوار پیشرفت
    const progressFill = $('#progressFill');
    if (progressFill) progressFill.style.width = `${((currentIndex + 1) / totalSlides) * 100}%`;

    // دکمه‌ها
    const prevBtn = $('#prevBtn');
    const nextBtn = $('#nextBtn');
    if (prevBtn) prevBtn.disabled = currentIndex === 0;
    if (nextBtn) nextBtn.disabled = currentIndex === totalSlides - 1;

    // Dots
    const slideDotsContainer = $('#slideDots');
    if (slideDotsContainer) {
      Array.from(slideDotsContainer.children).forEach((d, idx) => {
        d.classList.toggle('active', idx === currentIndex);
      });
    }

    // Drawer
    const drawerList = $('#drawerList');
    if (drawerList) {
      Array.from(drawerList.children).forEach((item, idx) => {
        item.classList.toggle('active', idx === currentIndex);
      });
    }

    // Chapter Nav
    const activeChapter = parseInt(slides[currentIndex].getAttribute('data-chapter') || '0', 10);
    $$('.chapter-btn').forEach((btn, idx) => {
      btn.classList.toggle('active', idx === activeChapter);
    });
  }

  // ═══════════════════════════════════════════
  // Navigation
  // ═══════════════════════════════════════════
  function goToSlide(index) {
    if (index < 0 || index >= totalSlides) return;
    currentIndex = index;
    updateDeckUI();
  }

  function nextSlide() {
    if (currentIndex < totalSlides - 1) {
      currentIndex++;
      updateDeckUI();
    }
  }

  function prevSlide() {
    if (currentIndex > 0) {
      currentIndex--;
      updateDeckUI();
    }
  }

  function toggleDrawer() {
    const drawer = $('#drawerBackdrop');
    if (drawer) drawer.classList.toggle('open');
  }

  function toggleFullScreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen().catch(() => {});
    }
  }

  // ═══════════════════════════════════════════
  // Card Flip Handlers
  // ═══════════════════════════════════════════
  window.toggleDebitCardFlip = function (el) {
    if (!el) el = $('#debitCardFlipper');
    if (el) el.classList.toggle('is-flipped');
  };

  window.toggleVoucherFlip = function (el) {
    if (el) el.classList.toggle('is-flipped');
  };

  // ═══════════════════════════════════════════
  // Keyboard Controls
  // ═══════════════════════════════════════════
  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) return;

    if (e.key === 'ArrowLeft' || e.key === 'PageDown' || e.key === ' ') {
      e.preventDefault();
      nextSlide();
    } else if (e.key === 'ArrowRight' || e.key === 'PageUp') {
      e.preventDefault();
      prevSlide();
    } else if (e.key === 'Home') {
      e.preventDefault();
      goToSlide(0);
    } else if (e.key === 'End') {
      e.preventDefault();
      goToSlide(totalSlides - 1);
    } else if (e.key === 'f' || e.key === 'F') {
      toggleFullScreen();
    } else if (e.key === 'Escape') {
      const drawer = $('#drawerBackdrop');
      if (drawer) drawer.classList.remove('open');
    }
  });

  // ═══════════════════════════════════════════
  // Iran Map Tooltip
  // ═══════════════════════════════════════════
  const MAP_DATA = [
    {"key":"Alborz","fa":"البرز","center":"کرج","stores":450},
    {"key":"Ardabil","fa":"اردبیل","center":"اردبیل","stores":65},
    {"key":"Bushehr","fa":"بوشهر","center":"بوشهر","stores":110},
    {"key":"ChaharmahalandBakhtiari","fa":"چهارمحال و بختیاری","center":"شهرکرد","stores":45},
    {"key":"EastAzerbaijan","fa":"آذربایجان شرقی","center":"تبریز","stores":420},
    {"key":"Fars","fa":"فارس","center":"شیراز","stores":480},
    {"key":"Gilan","fa":"گیلان","center":"رشت","stores":280},
    {"key":"Golestan","fa":"گلستان","center":"گرگان","stores":85},
    {"key":"Hamadan","fa":"همدان","center":"همدان","stores":80},
    {"key":"Hormozgan","fa":"هرمزگان","center":"بندرعباس","stores":190},
    {"key":"Ilam","fa":"ایلام","center":"ایلام","stores":25},
    {"key":"Isfahan","fa":"اصفهان","center":"اصفهان","stores":550},
    {"key":"Kerman","fa":"کرمان","center":"کرمان","stores":220},
    {"key":"Kermanshah","fa":"کرمانشاه","center":"کرمانشاه","stores":210},
    {"key":"Khuzestan","fa":"خوزستان","center":"اهواز","stores":350},
    {"key":"KohgiluyehAndBoyerAhmad","fa":"کهگیلویه و بویراحمد","center":"یاسوج","stores":30},
    {"key":"Kurdistan","fa":"کردستان","center":"سنندج","stores":90},
    {"key":"Lorestan","fa":"لرستان","center":"خرم‌آباد","stores":70},
    {"key":"Markazi","fa":"مرکزی","center":"اراک","stores":140},
    {"key":"Mazandaran","fa":"مازندران","center":"ساری","stores":170},
    {"key":"NorthKhorasan","fa":"خراسان شمالی","center":"بجنورد","stores":40},
    {"key":"Qazvin","fa":"قزوین","center":"قزوین","stores":150},
    {"key":"Qom","fa":"قم","center":"قم","stores":240},
    {"key":"RazaviKhorasan","fa":"خراسان رضوی","center":"مشهد","stores":700},
    {"key":"Semnan","fa":"سمنان","center":"سمنان","stores":50},
    {"key":"SistanAndBaluchestan","fa":"سیستان و بلوچستان","center":"زاهدان","stores":100},
    {"key":"SouthKhorasan","fa":"خراسان جنوبی","center":"بیرجند","stores":35},
    {"key":"Tehran","fa":"تهران","center":"تهران","stores":3200},
    {"key":"WestAzerbaijan","fa":"آذربایجان غربی","center":"ارومیه","stores":160},
    {"key":"Yazd","fa":"یزد","center":"یزد","stores":180},
    {"key":"Zanjan","fa":"زنجان","center":"زنجان","stores":55}
  ];

  function initMapTooltips() {
    const svg = $('.imap-svg');
    const box = $('.imap-map');
    if (!svg || !box) return;

    const byKey = {};
    MAP_DATA.forEach(m => byKey[m.key] = m);

    let tip = document.getElementById('imapTip');
    if (!tip) {
      tip = document.createElement('div');
      tip.id = 'imapTip';
      tip.className = 'imap-tip-rich';
      box.appendChild(tip);
    }

    const FA = '۰۱۲۳۴۵۶۷۸۹';
    function fa(n) {
      return n.toLocaleString('en-US').replace(/,/g, '٬').replace(/[0-9]/g, d => FA[+d]);
    }

    function show(el, x, y) {
      const m = byKey[el.getAttribute('data-k')];
      if (!m) return;
      const b = box.getBoundingClientRect();
      tip.innerHTML = `
        <div class="tip-title-row">
          <span class="tip-prov-name">استان ${m.fa}</span>
          <span class="tip-city-name">مرکز: ${m.center || '—'}</span>
        </div>
        <div class="tip-merch-row">
          <span>تعداد مرچنت:</span>
          <strong class="tip-merch-num">${m.stores ? fa(m.stores) : '۰'} فروشگاه</strong>
        </div>
      `;
      tip.style.left = (x - b.left) + 'px';
      tip.style.top = (y - b.top) + 'px';
      tip.classList.add('show');
    }

    svg.querySelectorAll('.imap-prov').forEach(p => {
      p.addEventListener('pointermove', e => show(p, e.clientX, e.clientY));
      p.addEventListener('click', e => show(p, e.clientX, e.clientY));
      p.addEventListener('pointerleave', () => tip.classList.remove('show'));
    });
  }

  // ═══════════════════════════════════════════
  // Card Expand (کلیک روی کارت‌ها در موبایل)
  // ═══════════════════════════════════════════
  function setupCardExpand() {
    $$('.glass-card:not(.no-collapse), .service-tile').forEach(box => {
      box.addEventListener('click', e => {
        if (e.target.closest('button, a, input, select, label')) return;
        box.classList.toggle('expanded-box');
      });
    });
  }

  // ═══════════════════════════════════════════
  // Export to Global (برای onclick ها در HTML)
  // ═══════════════════════════════════════════
  window.goToSlide = goToSlide;
  window.nextSlide = nextSlide;
  window.prevSlide = prevSlide;
  window.toggleDrawer = toggleDrawer;
  window.toggleFullScreen = toggleFullScreen;

  // ═══════════════════════════════════════════
  // Async Bootstrap (منتظر کامپوننت‌ها و اسلایدها)
  // ═══════════════════════════════════════════
  let componentsReady = false;
  let slidesReady = false;

  function tryInit() {
    if (componentsReady && slidesReady) {
      initDeck();
    }
  }

  window.addEventListener('componentsLoaded', () => {
    componentsReady = true;
    tryInit();
  });

  window.addEventListener('slidesLoaded', () => {
    slidesReady = true;
    tryInit();
  });

  // اگر قبلاً لود شده بودن (مثلاً صفحه رفرش شده)
  if (document.getElementById('chapterNav')) {
    componentsReady = true;
    tryInit();
  }
  if (document.querySelectorAll('.slide').length > 0) {
    slidesReady = true;
    tryInit();
  }
})();
```

=== ./js/components-loader.js ===

```javascript
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Components Loader
   بارگذاری داینامیک Header, Footer, Drawer
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const COMPONENTS = [
  { file: 'drawer.html', target: '#drawerSlot' }
  ];

  async function loadComponent({ file, target }) {
    try {
      const response = await fetch('components/' + file);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const html = await response.text();
      const el = document.querySelector(target);
      if (el) el.innerHTML = html;
    } catch (err) {
      console.error(`[ComponentsLoader] خطا در بارگذاری ${file}:`, err);
    }
  }

  async function initComponents() {
    await Promise.all(COMPONENTS.map(loadComponent));
    console.log('✅ Header, Footer, Drawer بارگذاری شدند.');
    window.dispatchEvent(new Event('componentsLoaded'));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initComponents);
  } else {
    initComponents();
  }
})();
async function initComponents() {
  await Promise.all(COMPONENTS.map(loadComponent));
  console.log('✅ Header, Footer, Drawer بارگذاری شدند.');
  window.componentsLoadedFlag = true;  // ← این خط رو اضافه کن
  window.dispatchEvent(new Event('componentsLoaded'));
}
```

=== ./js/slides-loader.js ===

```javascript
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Slides Loader Engine
   ───────────────────────────────────────────────────────────────
   • بارگذاری داینامیک اسلایدها از پوشه slides/
   • رندر درون main#stageContainer
   • ارسال رویداد slidesLoaded برای هماهنگی با navigation.js
   • اسلایدهای گم‌شده نادیده گرفته می‌شن (بدون پیام خطا در UI)
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // 📋 لیست تمام فایل‌های اسلاید (به ترتیب نمایش)
  const SLIDES_MANIFEST = [
    'slide-01-hero.html',
    'slide-02-ecosystem.html',
    'slide-03-ebcom.html',
    'slide-04-services.html',
    'slide-05-brands.html',
    'slide-06-challenges.html',
    'slide-07-ebcom-credit.html',
    'slide-08-pwa-demo.html',
    'slide-09-features.html',
    'slide-10-calculator.html',
    'slide-11-journey-1.html',
    'slide-12-journey-2.html',
    'slide-13-journey-3.html',
    'slide-14-journey-4.html',
    'slide-15-journey-5.html',
    'slide-16-welfare.html',
    'slide-17-overcharge.html',
    'slide-18-settlement.html',
    'slide-19-cash-solution.html',
    'slide-20-map.html',
    'slide-21-clients.html'
  ];

  const BASE_PATH = 'slides/';
  const container = document.getElementById('stageContainer');

  async function loadSlide(file) {
    try {
      const response = await fetch(BASE_PATH + file);
      if (!response.ok) {
        // ❌ خطا رو فقط توی کنسول لاگ کن، به DOM چیزی اضافه نکن
        console.warn(`[SlidesLoader] ${file} پیدا نشد (HTTP ${response.status}) — نادیده گرفته شد`);
        return null;
      }
      return await response.text();
    } catch (err) {
      // ❌ خطای شبکه یا CORS — فقط لاگ کن
      console.warn(`[SlidesLoader] ${file} بارگذاری نشد — نادیده گرفته شد:`, err.message);
      return null;
    }
  }

  async function initSlides() {
    if (!container) {
      console.error('[SlidesLoader] #stageContainer پیدا نشد!');
      return;
    }

    // بارگذاری موازی
    const results = await Promise.all(SLIDES_MANIFEST.map(loadSlide));

    // ✅ فیلتر کردن اسلایدهای گم‌شده (null)
    const validSlides = results.filter(html => html !== null);
    const missingCount = results.length - validSlides.length;

    // اگه هیچ اسلایدی لود نشد، پیام خطا بده
    if (validSlides.length === 0) {
      container.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; height:100%; color:#F16273; font-family:Vazirmatn; text-align:center; padding:40px;">
          <div>
            <h2 style="margin-bottom:12px;">اسلایدی بارگذاری نشد</h2>
            <p style="color:#94A3B8;">لطفاً با سرور محلی اجرا کن: <code style="background:#1F2933; padding:4px 10px; border-radius:6px;">python -m http.server 8000</code></p>
          </div>
        </div>`;
      console.error('[SlidesLoader] هیچ اسلایدی بارگذاری نشد!');
      window.dispatchEvent(new Event('slidesLoaded'));
      return;
    }

    // تزریق اسلایدها
    container.innerHTML = validSlides.join('');

    // تنظیم اسلاید اول به‌عنوان active
    const firstSlide = container.querySelector('.slide');
    if (firstSlide) firstSlide.classList.add('active');

    // لاگ نهایی
    if (missingCount > 0) {
      console.warn(`⚠️ ${validSlides.length} اسلاید بارگذاری شد — ${missingCount} فایل پیدا نشد (نادیده گرفته شد)`);
    } else {
      console.log(`✅ ${validSlides.length} اسلاید با موفقیت بارگذاری شد.`);
    }

    // ارسال رویداد برای navigation.js
    window.dispatchEvent(new Event('slidesLoaded'));
  }

  // اجرا
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSlides);
  } else {
    initSlides();
  }
})();
```

=== ./js/calculator.js ===

```javascript
/* ═══════════════════════════════════════════════════════════════
   EWANO B2B — Purchase Credit Calculator Engine
   ═══════════════════════════════════════════════════════════════ */

(function() {
  const root = document.getElementById('creditCalc');
  if (!root) return;

  const FA = '۰۱۲۳۴۵۶۷۸۹';
  const INSTALLMENT_OPTIONS = [4, 6, 12, 18, 24];
  
  const el = {
    amount: document.getElementById('calcAmount'),
    countIdx: document.getElementById('calcCountIdx'),
    feeRate: document.getElementById('calcFeeRate'),
    feeInput: document.getElementById('calcFeeInput'),
    amountOut: document.getElementById('calcAmountOut'),
    countOut: document.getElementById('calcCountOut'),
    feeOut: document.getElementById('calcFeeOut'),
    inst: document.getElementById('calcInst'),
    formula: document.getElementById('calcFormulaText'),
    resBase: document.getElementById('calcResBase'),
    resFee: document.getElementById('calcResFee'),
    resCount: document.getElementById('calcResCount'),
    resTotal: document.getElementById('calcResTotal')
  };

  const fa = n => Math.round(n).toLocaleString('en-US').replace(/,/g, '٬').replace(/[0-9]/g, d => FA[+d]);
  const faDec = n => String(n).replace('.', '٫').replace(/[0-9]/g, d => FA[+d]);

  function renderTicks(r, labels) {
    const box = r.parentNode.querySelector('.calc-ticks');
    if (!box) return;
    const min = +r.min, max = +r.max, step = +r.step;
    const n = labels ? labels.length : Math.round((max - min) / step) + 1;
    
    if (box.children.length !== n) {
      box.innerHTML = '';
      for (let k = 0; k < n; k++) {
        const d = document.createElement('i'), b = document.createElement('b');
        b.textContent = labels ? labels[k] : fa((min + k * step) / 1e6);
        d.appendChild(b);
        box.appendChild(d);
      }
    }
    
    const curVal = +r.value;
    for (let j = 0; j < n; j++) {
      const v = labels ? j : (min + j * step);
      box.children[j].className = v < curVal ? 'on' : Math.abs(v - curVal) < 0.001 ? 'cur' : '';
    }
  }

  function updateTrackFill(r, mode) {
    const f = (+r.value - +r.min) / (+r.max - +r.min);
    r.parentNode.style.setProperty('--f', f);
    
    if (mode === 'amount') renderTicks(r, null);
    else if (mode === 'count') renderTicks(r, ['۴ ماهه', '۶ ماهه', '۱۲ ماهه', '۱۸ ماهه', '۲۴ ماهه']);
    else if (mode === 'fee') {
      const marks = [0, 1, 1.9, 3, 4];
      const box = r.parentNode.querySelector('.calc-ticks');
      if (box.children.length !== marks.length) {
        box.innerHTML = '';
        marks.forEach(m => {
          const d = document.createElement('i'), b = document.createElement('b');
          b.textContent = faDec(m) + '٪';
          d.appendChild(b);
          box.appendChild(d);
        });
      }
      const cur = +r.value;
      marks.forEach((m, idx) => {
        box.children[idx].className = m < cur ? 'on' : Math.abs(m - cur) < 0.05 ? 'cur' : '';
      });
    }
  }

  function updateCalculator() {
    const principal = +el.amount.value;
    const count = INSTALLMENT_OPTIONS[+el.countIdx.value] || 12;
    const feePct = +el.feeRate.value;
    
    const basePerMonth = principal / count;
    const feePerMonth = principal * (feePct / 100);
    const installment = basePerMonth + feePerMonth;
    const totalRepayment = installment * count;

    updateTrackFill(el.amount, 'amount');
    updateTrackFill(el.countIdx, 'count');
    updateTrackFill(el.feeRate, 'fee');

    el.amountOut.innerHTML = fa(principal) + '<small>تومان</small>';
    el.countOut.innerHTML = fa(count) + '<small>قسط ماهانه</small>';
    el.feeOut.innerHTML = faDec(feePct.toFixed(1).replace(/\.0$/, '')) + '<small>٪ ماهانه</small>';

    el.inst.textContent = fa(installment);
    el.formula.textContent = `(${principal.toLocaleString('en-US')} ÷ ${count}) + (${principal.toLocaleString('en-US')} × ${feePct}%) = ${Math.round(installment).toLocaleString('en-US')}`;

    el.resBase.textContent = fa(basePerMonth) + ' تومان';
    el.resFee.textContent = feePct > 0 ? (fa(feePerMonth) + ' تومان') : 'بدون کارمزد (۰ تومان)';
    el.resCount.textContent = fa(count) + ' ماهه · کارمزد ' + faDec(feePct) + '٪';
    el.resTotal.textContent = fa(totalRepayment) + ' تومان';
  }

  // Event Listeners
  el.amount.addEventListener('input', updateCalculator);
  el.countIdx.addEventListener('input', updateCalculator);
  
  el.feeRate.addEventListener('input', () => {
    el.feeInput.value = el.feeRate.value;
    updateCalculator();
  });
  
  el.feeInput.addEventListener('input', () => {
    const v = parseFloat(el.feeInput.value);
    if (!isNaN(v) && v >= 0 && v <= 10) {
      el.feeRate.value = Math.min(4, Math.max(0, v));
      updateCalculator();
    }
  });

  window.setCalcPreset = function(amt, cIdx, fee) {
    el.amount.value = amt;
    el.countIdx.value = cIdx;
    el.feeRate.value = fee;
    el.feeInput.value = fee;
    updateCalculator();
  };

  updateCalculator();
})();
```

=== ./slides/slide-07-ebcom-credit.html ===

```html
<!-- =====================================================================
     SLIDE 7: EBCOM CREDIT & ORGANIZATIONAL WELFARE
     ===================================================================== -->

<section
  class="slide active"
  data-chapter="1"
  data-title="راهکارهای اعتباری EBCOM و رفاهیات سازمانی">
  <div class="slide-inner">
    <!-- Header -->
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"> فصل دوم · معماری راهکار سازمانی </span>

      <span style="font-size: 12px; color: var(--text-muted)">
        تلفیق زیرساخت مالی EBCOM با شبکه گسترده پذیرندگان
      </span>
    </div>

    <!-- Main Title -->
    <h2 class="slide-headline anim-up delay-2">
      راهکارهای اعتباری
      <span class="accent-green">EBCOM</span>
      و مدیریت متمرکز
      <span class="accent-orange">رفاهیات سازمانی</span>
    </h2>

    <!-- Main Content -->
    <div class="grid-2 slide7-aligned-grid anim-up delay-3">
      <!-- Right Column: EBCOM -->
      <div class="glass-card slide7-right-box">
        <span class="eyebrow-badge" style="align-self: flex-start">
          زیرساخت مالی و اعتباری EBCOM
        </span>

        <h3 class="s7-main-title">تأمین و مدیریت منعطف اعتبار سازمانی</h3>

        <p class="s7-main-text">
          <strong>EBCOM</strong>
          با بهره‌گیری از زیرساخت مالی و اعتباری خود، راهکارهایی منعطف و قابل
          مدیریت برای تأمین اعتبار کاربران، کسب‌وکارها و سازمان‌ها ارائه می‌کند.
          این راهکارها به سازمان‌ها امکان می‌دهند اعتبار را متناسب با سیاست‌های
          خود تخصیص داده و مدیریت کنند و در عین حال، کارکنان از شبکه متنوع
          پذیرندگان و آزادی انتخاب بهره‌مند شوند.
        </p>

        <!-- Organization Flow -->
        <div class="s7-flow">
          <!-- Node 1: Organization -->
          <div class="s7-flow-node">
            <div class="s7-node s7-node-outline-green">سازمان</div>

            <span class="s7-node-label"> تعریف سیاست </span>
          </div>

          <!-- Flow Line 1 -->
          <div class="s7-flow-line">
            <svg
              viewBox="0 0 100 20"
              preserveAspectRatio="none"
              aria-hidden="true">
              <line
                x1="2"
                y1="10"
                x2="98"
                y2="10"
                stroke="#00D4B4"
                stroke-width="3"
                stroke-dasharray="6 4"
                class="svg-flow-line" />
            </svg>
          </div>

          <!-- Node 2: Avano -->
          <div class="s7-flow-node">
            <div class="s7-node s7-node-green">اوانو</div>

            <span class="s7-node-label s7-node-label-green">
              تخصیص هوشمند
            </span>
          </div>

          <!-- Flow Line 2 -->
          <div class="s7-flow-line">
            <svg
              viewBox="0 0 100 20"
              preserveAspectRatio="none"
              aria-hidden="true">
              <line
                x1="2"
                y1="10"
                x2="98"
                y2="10"
                stroke="#FF7722"
                stroke-width="3"
                stroke-dasharray="6 4"
                class="svg-flow-line" />
            </svg>
          </div>

          <!-- Node 3: Employees -->
          <div class="s7-flow-node">
            <div class="s7-node s7-node-outline-orange">کارکنان</div>

            <span class="s7-node-label"> آزادی انتخاب </span>
          </div>
        </div>
      </div>

      <!-- Left Column: Organizational Welfare -->
      <div class="slide7-left-stack">
        <!-- Item 1 -->
        <div class="glass-card slide7-left-item">
          <div class="s7-item-num s7-num-green">۱</div>

          <div class="s7-item-body">
            <h4 class="s7-item-title">مدیریت متمرکز اعتبارات رفاهی</h4>

            <p class="s7-item-text">
              کنترل یکپارچه تمام منابع رفاهی سازمان در یک پنل اختصاصی
            </p>
          </div>
        </div>

        <!-- Item 2 -->
        <div class="glass-card slide7-left-item">
          <div class="s7-item-num s7-num-orange">۲</div>

          <div class="s7-item-body">
            <h4 class="s7-item-title">
              تخصیص انعطاف‌پذیر متناسب با سیاست‌های سازمان
            </h4>

            <p class="s7-item-text">
              امکان تعریف اعتبار بر اساس سنوات، جایگاه سازمانی و گروه‌های پرسنلی
            </p>
          </div>
        </div>

        <!-- Item 3 -->
        <div class="glass-card slide7-left-item">
          <div class="s7-item-num s7-num-sky">۳</div>

          <div class="s7-item-body">
            <h4 class="s7-item-title">
              گستره متنوع پذیرندگان و آزادی انتخاب برای کارکنان
            </h4>

            <p class="s7-item-text">
              دسترسی بی‌مرز به هزاران فروشگاه زنجیره‌ای، آنلاین و مراکز خرید
            </p>
          </div>
        </div>

        <!-- Item 4 -->
        <div class="glass-card slide7-left-item">
          <div class="s7-item-num s7-num-purple">۴</div>

          <div class="s7-item-body">
            <h4 class="s7-item-title">
              کاهش پیچیدگی اجرایی و بهبود تجربه دریافت و مصرف مزایا
            </h4>

            <p class="s7-item-text">
              حذف فرآیندهای کاغذی و تسویه سنتی با رضایت حداکثری کارکنان
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-05-brands.html ===

```html
<section
  class="slide active"
  data-chapter="0"
  data-title="شرکای تجاری کیف پول اوانو (۲۵ برند برتر)">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل اول · اکوسیستم پذیرندگی</span>
      <span class="slide-top-meta-hint">منبع: تیم توسعه کسب‌وکار اوانو</span>
    </div>

    <h2 class="slide-headline anim-up delay-2">
      شرکای تجاری کیف پول <span class="accent-green">اوانو</span>؛ حضور برترین
      برندهای ایران
    </h2>

    <div class="brands-25-grid anim-up delay-3">
      <div class="brand-tile" style="--brand-color: #00d170">
        <span class="brand-logo-slot"
          ><img src="./assets/snapp.svg" alt="اسنپ (Snapp!)"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اسنپ (Snapp!)</span>
          <span class="brand-tile-cat">سوپراپ</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #9c27b0">
        <span class="brand-logo-slot"
          ><img src="./assets/snapp-shop.svg" alt="اسنپ‌شاپ"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اسنپ‌شاپ</span>
          <span class="brand-tile-cat">فروشگاه آنلاین</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ff00a6">
        <span class="brand-logo-slot"
          ><img src="./assets/snapp-food.svg" alt="اسنپ‌فود (Food!)"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اسنپ‌فود (Food!)</span>
          <span class="brand-tile-cat">سفارش غذا</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ff6600">
        <span class="brand-logo-slot"
          ><img src="./assets/snapp-market.svg" alt="اسنپ‌ مارکت"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اسنپ‌مارکت</span>
          <span class="brand-tile-cat">سوپرمارکت</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #00aeef">
        <span class="brand-logo-slot"
          ><img src="./assets/snapp-dr.svg" alt="اسنپ‌دکتر"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اسنپ‌دکتر</span>
          <span class="brand-tile-cat">سلامت و دارو</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ff2a2a">
        <span class="brand-logo-slot"
          ><img src="./assets/snapp-trip.svg" alt="اسنپ‌تریپ"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اسنپ‌تریپ</span>
          <span class="brand-tile-cat">سفر و هتل</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ef394e">
        <span class="brand-logo-slot"
          ><img src="./assets/digikala.svg" alt="دیجی‌کالا"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">دیجی‌کالا</span>
          <span class="brand-tile-cat">خرده‌فروشی آنلاین</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ff7722">
        <span class="brand-logo-slot"
          ><img src="./assets/digikala-jet.svg" alt="دیجی‌کالا جت"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">دیجی‌کالا جت</span>
          <span class="brand-tile-cat">تحویل فوری</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ff5722">
        <span class="brand-logo-slot"
          ><img src="./assets/tapsi-shop.svg" alt="تپسی‌شاپ"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">تپسی‌شاپ</span>
          <span class="brand-tile-cat">فروشگاه آنلاین</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #e31e24">
        <span class="brand-logo-slot"
          ><img src="./assets/ofogh-koorosh.svg" alt="افق کوروش"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">افق کوروش</span>
          <span class="brand-tile-cat">۲٬۸۰۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #e53935">
        <span class="brand-logo-slot"
          ><img src="./assets/hyper-star.svg" alt="هایپراستار"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">هایپراستار</span>
          <span class="brand-tile-cat">هایپرمارکت</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #00acc1">
        <span class="brand-logo-slot"
          ><img src="./assets/hyper-family.svg" alt="هایپر فمیلی"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">هایپر فمیلی</span>
          <span class="brand-tile-cat">۸۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #fbc02d">
        <span class="brand-logo-slot"
          ><img src="./assets/hyper-mi.svg" alt="هایپرمی"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">هایپرمی</span>
          <span class="brand-tile-cat">۲۶ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #00897b">
        <span class="brand-logo-slot"
          ><img src="./assets/refah.svg" alt="فروشگاه‌های رفاه"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">فروشگاه‌های رفاه</span>
          <span class="brand-tile-cat">۷۰۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #d32f2f">
        <span class="brand-logo-slot"
          ><img src="./assets/shahrvand.svg" alt="فروشگاه شهروند"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">فروشگاه شهروند</span>
          <span class="brand-tile-cat">۵۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #43a047">
        <span class="brand-logo-slot"
          ><img src="./assets/daily-market.svg" alt="دیلی‌مارکت"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">دیلی‌مارکت</span>
          <span class="brand-tile-cat">۱٬۴۰۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #8e24aa">
        <span class="brand-logo-slot"
          ><img src="./assets/gandom.svg" alt="فروشگاه گندم"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">فروشگاه گندم</span>
          <span class="brand-tile-cat">۷۵۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #1e88e5">
        <span class="brand-logo-slot"
          ><img src="./assets/haft.svg" alt="فروشگاه هفت"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">فروشگاه هفت</span>
          <span class="brand-tile-cat">۶۰۰ شعبه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #00bfa5">
        <span class="brand-logo-slot"
          ><img src="./assets/achare.svg" alt="آچاره"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">آچاره</span>
          <span class="brand-tile-cat">خدمات منزل</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #1565c0">
        <span class="brand-logo-slot"
          ><img src="./assets/technolife.svg" alt="تکنولایف"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">تکنولایف</span>
          <span class="brand-tile-cat">کالای دیجیتال</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #e91e63">
        <span class="brand-logo-slot"
          ><img src="./assets/okala.svg" alt="اُکالا (Okala)"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">اُکالا (Okala)</span>
          <span class="brand-tile-cat">سوپرمارکت آنلاین</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #ffd54f">
        <span class="brand-logo-slot"
          ><img src="./assets/talasea.svg" alt="طلاسی"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">طلاسی</span>
          <span class="brand-tile-cat">خرید آنلاین طلا</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #0288d1">
        <span class="brand-logo-slot"
          ><img src="./assets/ebcom.svg" alt="فلای تودی"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">فلای‌تودی</span>
          <span class="brand-tile-cat">پرواز و هتل</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #26a69a">
        <span class="brand-logo-slot"
          ><img src="./assets/fidilio.svg" alt="فیدیلیو"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">فیدیلیو</span>
          <span class="brand-tile-cat">رستوران و کافه</span>
        </div>
      </div>

      <div class="brand-tile" style="--brand-color: #3949ab">
        <span class="brand-logo-slot"
          ><img src="./assets/shab.svg" alt="شب (Shab)"
        /></span>
        <div class="brand-tile-info">
          <span class="brand-tile-name">شب (Shab)</span>
          <span class="brand-tile-cat">اجاره اقامتگاه</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-20-map.html ===

```html
<div class="network-map-grid s20-map-grid anim-up delay-3">

  <!-- ستون چپ: نقشه -->
  <div class="s20-map-col">
    <div class="imap">
      <div class="imap-map s20-imap-map">
        <svg class="imap-svg s20-imap-svg" viewBox="0 0 1000 904" role="group" aria-label="نقشهٔ ۳۱ استان ایران">
          <!-- ✅ محتوای SVG نقشه رو از فایل اصلی کپی کن (دست نزن) -->
        </svg>

        <div class="imap-tip" aria-hidden="true"></div>
        <div class="imap-legend">
          <span><i class="t4"></i>بیش از ۱,۰۰۰</span>
          <span><i class="t3"></i>۴۰۰ تا ۱,۰۰۰</span>
          <span><i class="t2"></i>۲۰۰ تا ۴۰۰</span>
          <span><i class="t1"></i>کمتر از ۲۰۰</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ستون راست: آمار -->
  <div class="s20-stats-col">

    <div class="s20-stats-grid">
      <div class="glass-card no-collapse s20-stat-card border-right-green">
        <h4 class="s20-stat-title text-green">۹٬۴۱۵ مرچنت و ۱۰٬۴۷۲ شعبه</h4>
        <p class="s20-stat-text">پوشش سراسری در ۳۱ استان کشور شامل ۳٬۹۷۷ برند حضوری و ۵٬۴۳۸ فروشگاه آنلاین فعال</p>
      </div>
      <div class="glass-card no-collapse s20-stat-card border-right-sky">
        <h4 class="s20-stat-title text-sky">۵٬۴۳۸ فروشگاه آنلاین (۵۷.۸٪)</h4>
        <p class="s20-stat-text">دیجی‌کالا، اسنپ، اسنپ‌فود، اُکالا، تکنولایف، فلای‌تودی، تپسی‌شاپ و شب</p>
      </div>
    </div>

    <div class="glass-card no-collapse s20-stat-card s20-stat-wide border-right-orange">
      <h4 class="s20-stat-title text-orange">۱۱ زنجیره بزرگ فروشگاهی (۶٬۵۶۱ شعبه کشوری)</h4>
      <p class="s20-stat-text">
        افق کوروش (<strong>۲٬۸۰۰ شعبه</strong>) · دیلی‌مارکت (<strong>۱٬۴۰۰ شعبه</strong>) · گندم (<strong>۷۵۰ شعبه</strong>) · رفاه (<strong>۷۰۰ شعبه</strong>) · هفت (<strong>۶۰۰ شعبه</strong>) · هایپرفمیلی (۸۰) · شهروند (۵۰) · هایپرمی (۲۶) · هایپراستار (۲۰)
      </p>
    </div>

    <div class="glass-card no-collapse s20-stat-card s20-stat-wide border-right-purple">
      <h4 class="s20-stat-title text-purple">۳٬۹۶۶ پذیرنده غیرزنجیره‌ای و ۶ مال برتر</h4>
      <p class="s20-stat-text">
        • <strong>ترکیب اصناف:</strong> پوشاک (۱٬۸۲۳) · کالای دیجیتال (۵۴۶) · خانه و آشپزخانه (۳۸۶) · طلا و زیورآلات (۳۴۳) · آرایشی بهداشتی (۳۰۵)<br>
        • <strong>مراکز خرید برتر:</strong> ایران‌مال (+۷۰۰ واحد)، اپال، سانا سنتر، مگامال، نیایش‌مال و بام‌لند
      </p>
    </div>

  </div>

</div>

<!-- Marquee پایین -->
<div class="anim-up delay-4 marquee-fade-wrapper s20-marquee">
  <div class="logo-dots">
    <!-- ✅ ۱۹ logo-dot رو از فایل اصلی کپی کن (دست نزن) -->
  </div>
</div>
```

=== ./slides/slide-03-ebcom.html ===

```html
<section
  class="slide active"
  data-chapter="0"
  data-title="درباره EBCOM و پلتفرم استراتژیک اوانو">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل اول · بازوی فین‌تک همراه اول</span>
      <span class="slide-top-meta-hint"
        >قابل استفاده برای کاربران تمامی اپراتورها</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      درباره <span class="accent-green">EBCOM</span> و جایگاه
      <span class="vessel-pill">اوانو</span>
    </h2>

    <div class="grid-2 slide3-equal-grid anim-up delay-3">
      <!-- کارت EBCOM -->
      <div class="glass-card slide3-equal-card border-top-green">
        <div class="s3-card-header">
          <span class="eyebrow-badge">EBCOM</span>
          <span class="s3-card-badge s3-card-badge-green"
            >بازوی تخصصی فین‌تک</span
          >
        </div>

        <h3 class="s3-card-title">
          توسعه اقتصاد دیجیتال و راهکارهای نوآورانه مالی
        </h3>

        <p class="s3-card-text">
          شرکت <strong>EBCOM</strong>، به‌عنوان بازوی فین‌تک همراه اول، با هدف
          توسعه اقتصاد دیجیتال و خلق ارزش از طریق راهکارهای نوآورانه در حوزه
          <strong>خدمات مالی، پرداخت و اعتبار</strong> فعالیت می‌کند. EBCOM با
          بهره‌گیری از ظرفیت‌های اکوسیستم همراه اول، مجموعه‌ای از محصولات و
          خدمات مالی و دیجیتال را برای کاربران، کسب‌وکارها و سازمان‌ها توسعه
          داده و تجاری‌سازی کرده است.
        </p>

        <div class="s3-features-grid">
          <div class="s3-feature-box s3-feature-green">
            <div class="s3-feature-title text-green">خدمات مالی</div>
            <p class="s3-feature-sub">کیف پول و بانکی</p>
          </div>
          <div class="s3-feature-box s3-feature-orange">
            <div class="s3-feature-title text-orange">راهکار اعتباری</div>
            <p class="s3-feature-sub">تأمین مالی و BNPL</p>
          </div>
          <div class="s3-feature-box s3-feature-sky">
            <div class="s3-feature-title text-sky">خدمات سازمانی</div>
            <p class="s3-feature-sub">رفاهیات و B2B</p>
          </div>
        </div>
      </div>

      <!-- کارت اوانو -->
      <div class="glass-card slide3-equal-card border-top-orange">
        <div class="s3-card-header">
          <span class="eyebrow-badge orange"
            >اوانو؛ پلتفرم استراتژیک EBCOM</span
          >
          <span class="s3-card-badge s3-card-badge-orange"
            >فراتر از یک اپراتور</span
          >
        </div>

        <h3 class="s3-card-title">
          خلق تجربه‌ای متفاوت از زندگی دیجیتال برای همه
        </h3>

        <p class="s3-card-text">
          <strong>اوانو</strong> پلتفرمی یکپارچه برای ارائه خدمات دیجیتال و مالی
          است که برای <strong>کاربران تمامی اپراتورها</strong> (همراه اول،
          ایرانسل، رایتل و...) قابل استفاده است. بر اساس برندبوک اوانو، مأموریت
          ما بر سه ستون کلیدی استوار است:
        </p>

        <div class="s3-features-grid">
          <div class="s3-feature-box s3-feature-green">
            <div class="s3-feature-title text-green">۱. دسترسی آسان</div>
            <p class="s3-feature-sub">خدمات متنوع در یک سوپراپ</p>
          </div>
          <div class="s3-feature-box s3-feature-orange">
            <div class="s3-feature-title text-orange">۲. ارائه اعتبار</div>
            <p class="s3-feature-sub">تأمین مالی منعطف و فوری</p>
          </div>
          <div class="s3-feature-box s3-feature-sky">
            <div class="s3-feature-title text-sky">۳. پرداخت هوشمند</div>
            <p class="s3-feature-sub">بارکدخوان، درگاه و کیف پول</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-16-welfare.html ===

```html
<section
  class="slide active"
  data-chapter="3"
  data-title="معرفی رفاهیات سازمانی و سرفصل‌های انتخابی">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل چهارم · رفاهیات سازمانی</span>
      <span class="slide-top-meta-hint"
        >تنوع سرفصل‌ها، گستره‌ای از پذیرندگان منتخب</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      معرفی <span class="accent-green">رفاهیات سازمانی</span>؛ سرفصل‌های انتخابی
      متناسب با هر سازمان
    </h2>

    <!-- پیل‌های ۷ دسته‌بندی رفاهی -->
    <div class="welfare-categories-strip s16-categories-strip anim-up delay-2">
      <span class="welfare-cat-pill wcat-active">۱. معیشتی</span>
      <span class="welfare-cat-pill">۲. رفاهی</span>
      <span class="welfare-cat-pill">۳. آموزشی</span>
      <span class="welfare-cat-pill">۴. بیمه</span>
      <span class="welfare-cat-pill wcat-orange">۵. آجیل و خشکبار</span>
      <span class="welfare-cat-pill wcat-orange">۶. اعیاد و مناسبت‌ها</span>
      <span class="welfare-cat-pill wcat-muted"
        >۷. سایر مزایای موردنیاز سازمان</span
      >
    </div>

    <!-- ۳ کارت showcase -->
    <div class="s16-showcases-grid anim-up delay-3">
      <!-- کارت ۱: بسته پروتئین و معیشتی -->
      <div class="glass-card s16-card s16-card-green">
        <span class="eyebrow-badge s16-card-badge">پذیرندگان منتخب</span>
        <h3 class="s16-card-title text-green">🥩 بسته پروتئین و معیشتی</h3>
        <p class="s16-card-text">
          امکان خرید انواع محصولات پروتئینی، سوپرمارکتی و کالاهای اساسی خانوار
          به صورت آنلاین و حضوری:
        </p>
        <div class="s16-brands-row">
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">د</span>
            <span>دهکده پروتئین</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/digikala.svg"
              alt="دیجی‌کالا"
              class="pill-brand-logo" />
            <span>دیجی‌کالا</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/okala.svg"
              alt="اُکالا"
              class="pill-brand-logo" />
            <span>اُکالا</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/hyperstar.svg"
              alt="هایپراستار"
              class="pill-brand-logo" />
            <span>هایپراستار</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/tapsi-shop.svg"
              alt="تپسی‌شاپ"
              class="pill-brand-logo" />
            <span>تپسی‌شاپ</span>
          </span>
        </div>
      </div>

      <!-- کارت ۲: آجیل، خشکبار و شیرینی -->
      <div class="glass-card s16-card s16-card-orange">
        <span class="eyebrow-badge orange s16-card-badge"
          >ویژه اعیاد و یلدا/نوروز</span
        >
        <h3 class="s16-card-title text-orange">🌰 آجیل، خشکبار و شیرینی</h3>
        <p class="s16-card-text">
          تخصیص بسته رفاهی مناسبتی برای خرید از معتبرترین برندهای آجیل و خشکبار
          کشور:
        </p>
        <div class="s16-brands-row">
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">آ</span>
            <span>آجیل و خشکبار محسن</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">خ</span>
            <span>خشکبار ایوب</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">آ</span>
            <span>آجیل اصل تبریز</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">ر</span>
            <span>رویال آجیل</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/okala.svg"
              alt="اُکالا"
              class="pill-brand-logo" />
            <span>اُکالا</span>
          </span>
        </div>
      </div>

      <!-- کارت ۳: کالای دیجیتال و الکترونیک -->
      <div class="glass-card s16-card s16-card-sky">
        <span class="eyebrow-badge sky s16-card-badge">تجهیز و رفاه پرسنل</span>
        <h3 class="s16-card-title text-sky">💻 کالای دیجیتال و الکترونیک</h3>
        <p class="s16-card-text">
          خرید موبایل، لپ‌تاپ، لوازم جانبی و گجت‌های هوشمند از برترین
          فروشگاه‌های دیجیتال کشور:
        </p>
        <div class="s16-brands-row">
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/digikala.svg"
              alt="دیجی‌کالا"
              class="pill-brand-logo" />
            <span>دیجی‌کالا</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/technolife.svg"
              alt="تکنولایف"
              class="pill-brand-logo" />
            <span>تکنولایف</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <img
              src="./assets/brands/tapsi-shop.svg"
              alt="تپسی‌شاپ"
              class="pill-brand-logo" />
            <span>تپسی‌شاپ</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">ز</span>
            <span>زرین‌پلاس</span>
          </span>
          <span class="co-pill brand-logo-pill">
            <span class="pill-brand-placeholder">پ</span>
            <span>پلازا دیجیتال</span>
          </span>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-21-clients.html ===

```html
<section class="slide" data-chapter="4" data-title="گزارش آماری اوانو، سازمان‌های همکار و جمع‌بندی چرا اوانو؟">
  <div class="slide-inner">

    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل پنجم · اعتماد سازمان‌های بزرگ و جمع‌بندی</span>
      <span class="text-sm text-green font-black">از تخصیص مزایا تا مصرف؛ یک تجربه یکپارچه برای سازمان و کارکنان</span>
    </div>

    <h2 class="slide-headline anim-up delay-2">
      چرا <span class="accent-green">اوانو</span>؟ زیرساخت یکپارچه برای ارائه مزایای سازمانی
    </h2>

    <!-- ۳ کارت آمار بالا -->
    <div class="s21-stats-grid anim-up delay-2">

      <div class="glass-card no-collapse s21-stat-card s21-stat-green">
        <div class="s21-stat-value">+۲۸ میلیون کاربر</div>
        <p class="s21-stat-label">بیش از ۸۵۰ هزار کاربر سازمانی فعال</p>
      </div>

      <div class="glass-card no-collapse s21-stat-card s21-stat-orange">
        <div class="s21-stat-value">+۲۰ همت خرید</div>
        <p class="s21-stat-label">گردش مالی و خرید در شبکه پذیرندگی</p>
      </div>

      <div class="glass-card no-collapse s21-stat-card s21-stat-sky">
        <div class="s21-stat-value">+۱۵ میلیون تراکنش</div>
        <p class="s21-stat-label">تراکنش ماهانه پایدار در سوپراپلیکیشن اوانو</p>
      </div>

    </div>

    <!-- پنل مشتریان -->
    <div class="glass-card no-collapse s21-clients-panel anim-up delay-3">

      <div class="s21-clients-head">
        <h3 class="s21-clients-title">
          <span class="s21-clients-emoji">🤝</span>
          <span>تجربه همکاری موفق با سازمان‌ها و نهادهای بزرگ کشور</span>
        </h3>
        <span class="s21-clients-badge">+۳۰۰ سازمان و شرکت همکار</span>
      </div>

      <div class="client-marquee-wrapper s21-marquee">

        <!-- ردیف ۱ — راست به چپ -->
        <div class="client-track-container track-row-1">
          <div class="client-track track-move-right">
            <div class="client-set">
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/hyperme.svg" alt="سازمان صدا و سیما"></div><div class="client-unit-name">سازمان صدا و سیما</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/refah.svg" alt="سازمان بیمه سلامت"></div><div class="client-unit-name">سازمان بیمه سلامت</div></div>
              <div class="client-org-unit"><div class="client-circle-logo placeholder-circle">و</div><div class="client-unit-name">وزارت نیرو</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/shahrvand.svg" alt="نهاد ریاست جمهوری"></div><div class="client-unit-name">نهاد ریاست جمهوری</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/naghsh-aval.svg" alt="همراه اول"></div><div class="client-unit-name">همراه اول</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/ebcom-2.svg" alt="مبین‌نت"></div><div class="client-unit-name">مبین‌نت</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/daily-market.svg" alt="هتل‌های هما"></div><div class="client-unit-name">هتل‌های هما</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/image-30.png" alt="انرژی گستر پاسارگاد"></div><div class="client-unit-name">انرژی گستر پاسارگاد</div></div>
              <div class="client-org-unit"><div class="client-circle-logo placeholder-circle">ب</div><div class="client-unit-name">بانک مسکن</div></div>
              <div class="client-org-unit"><div class="client-circle-logo placeholder-circle">ج</div><div class="client-unit-name">جیرینگ</div></div>
            </div>
          </div>
        </div>

        <!-- ردیف ۲ — چپ به راست -->
        <div class="client-track-container track-row-2">
          <div class="client-track track-move-left">
            <div class="client-set">
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/image-31.png" alt="گروه مالی کارآمد"></div><div class="client-unit-name">گروه مالی کارآمد</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/voucher-2.png" alt="سازمان بهسا"></div><div class="client-unit-name">سازمان بهسا</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/image-32.png" alt="فناپ"></div><div class="client-unit-name">فناپ</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/gandom.svg" alt="آسیاتک"></div><div class="client-unit-name">آسیاتک</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/haft.svg" alt="تالیا"></div><div class="client-unit-name">تالیا</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/achareh.svg" alt="سازمان انرژی اتمی"></div><div class="client-unit-name">سازمان انرژی اتمی</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/image-33.png" alt="دامپزشکی کشور"></div><div class="client-unit-name">دامپزشکی کشور</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/logos/partners/behpardaz-jahan.webp" alt="بهپرداز جهان"></div><div class="client-unit-name">بهپرداز جهان</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/image-34.png" alt="اموال و املاک کوثر"></div><div class="client-unit-name">اموال و املاک کوثر</div></div>
              <div class="client-org-unit"><div class="client-circle-logo"><img src="assets/images/cards/image-35.png" alt="حوزه هنری"></div><div class="client-unit-name">حوزه هنری</div></div>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- ۵ ستون چرا اوانو -->
    <div class="s21-pillars-grid anim-up delay-4">

      <div class="glass-card no-collapse why-pillar-card s21-pillar s21-pillar-green">
        <div class="why-pillar-title text-green">۱. یکپارچه</div>
        <p class="why-pillar-desc">مدیریت نقدی، اعتباری و رفاهی در یک پلتفرم واحد</p>
      </div>

      <div class="glass-card no-collapse why-pillar-card s21-pillar s21-pillar-orange">
        <div class="why-pillar-title text-orange">۲. منعطف</div>
        <p class="why-pillar-desc">متناسب با سیاست و نیاز اختصاصی هر سازمان</p>
      </div>

      <div class="glass-card no-collapse why-pillar-card s21-pillar s21-pillar-sky">
        <div class="why-pillar-title text-sky">۳. گسترده</div>
        <p class="why-pillar-desc">شبکه متنوع ۹٬۴۱۵ پذیرنده حضوری و آنلاین</p>
      </div>

      <div class="glass-card no-collapse why-pillar-card s21-pillar s21-pillar-pastel">
        <div class="why-pillar-title s21-pastel-text">۴. قابل مدیریت</div>
        <p class="why-pillar-desc">کنترل، گزارش‌گیری لحظه‌ای و شفافیت مالی</p>
      </div>

      <div class="glass-card no-collapse why-pillar-card s21-pillar s21-pillar-purple">
        <div class="why-pillar-title s21-purple-text">۵. کاربرمحور</div>
        <p class="why-pillar-desc">انتخاب بیشتر و تجربه ساده‌تر برای کارکنان</p>
      </div>

    </div>

  </div>
</section>
```

=== ./slides/slide-11-journey-1.html ===

```html
<section
  class="slide active"
  data-chapter="2"
  data-title="مسیر اعتبار (گام ۱ از ۶): شارژ اعتبار پرسنل">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل سوم · مسیر استفاده از اعتبار سازمانی (گام ۱ از ۶)</span
      >
      <span class="slide-top-meta-formula"
        >از شارژ اعتبار تا تسویه کامل، شفاف و قابل پیش‌بینی</span
      >
    </div>

    <!-- ریل پیشرفت ۶ مرحله‌ای -->
    <div class="journey-progress-rail anim-up delay-2">
      <div class="rail-step current" onclick="goToSlide(10)">
        <div class="rail-num">۱</div>
        <div class="rail-label">شارژ اعتبار پرسنل</div>
      </div>
      <div class="rail-step" onclick="goToSlide(11)">
        <div class="rail-num">۲</div>
        <div class="rail-label">استفاده و خرید</div>
      </div>
      <div class="rail-step" onclick="goToSlide(12)">
        <div class="rail-num">۳</div>
        <div class="rail-label">صدور صورتحساب و تنفس</div>
      </div>
      <div class="rail-step" onclick="goToSlide(13)">
        <div class="rail-num">۴</div>
        <div class="rail-label">پرداخت اولین قسط</div>
      </div>
      <div class="rail-step" onclick="goToSlide(14)">
        <div class="rail-num">۵</div>
        <div class="rail-label">روز معرفی به سازمان</div>
      </div>
      <div class="rail-step" onclick="goToSlide(15)">
        <div class="rail-num">۶</div>
        <div class="rail-label">روز تسویه سازمان</div>
      </div>
    </div>

    <div class="step-hero-panel s11-panel anim-up delay-3">
      <!-- کارت اصلی -->
      <div class="glass-card s11-main-card s11-main-card-green">
        <div class="s11-badge-row">
          <span class="s11-step-badge">گام اول</span>
          <span class="s11-step-hint">شروع چرخه اعتبار سازمانی</span>
        </div>

        <h2 class="s11-main-title">۱. شارژ اعتبار پرسنل توسط سازمان</h2>

        <p class="s11-main-text">
          در گام نخست، سازمان بر اساس سیاست‌های داخلی خود (نظیر سنوات، سطح حقوق
          یا جایگاه سازمانی)، لیست پرسنل و سقف اعتبار هر فرد را مشخص می‌کند و
          <strong>اعتبار به صورت آنی در کیف پول اعتباری اوانو</strong>
          کارکنان شارژ و فعال می‌شود.
        </p>

        <div class="s11-tips-grid">
          <div class="s11-tip-box">
            <div class="s11-tip-title">✓ فعال‌سازی آنی و بدون کاغذبازی</div>
            <div class="s11-tip-sub">
              اطلاع‌رسانی پیامکی فوری به هر کارمند پس از شارژ کیف پول
            </div>
          </div>
          <div class="s11-tip-box">
            <div class="s11-tip-title">✓ گروه‌بندی منعطف پرسنل</div>
            <div class="s11-tip-sub">
              تخصیص مبالغ متفاوت به مدیران، کارشناسان و واحدهای عملیاتی
            </div>
          </div>
        </div>
      </div>

      <!-- ستون ویژوال -->
      <div class="glass-card step-visual-box s11-visual-box">
        <svg class="s11-visual-svg" viewBox="0 0 260 220">
          <circle
            cx="130"
            cy="110"
            r="82"
            fill="rgba(0,212,180,0.12)"
            class="svg-pulse"></circle>
          <rect
            x="75"
            y="55"
            width="110"
            height="110"
            rx="24"
            fill="#171F26"
            stroke="#00D4B4"
            stroke-width="3"></rect>
          <path
            d="M105 140V85l25-15 25 15v55"
            fill="none"
            stroke="#00D4B4"
            stroke-width="3.5"
            stroke-linejoin="round"></path>
          <line
            x1="95"
            y1="140"
            x2="165"
            y2="140"
            stroke="#00D4B4"
            stroke-width="3.5"
            stroke-linecap="round"></line>
          <rect
            x="120"
            y="95"
            width="20"
            height="15"
            rx="2"
            fill="#FF7722"></rect>
          <rect x="122" y="120" width="16" height="20" fill="#00D4B4"></rect>
        </svg>
        <div class="s11-visual-title">تخصیص اعتبار توسط سازمان به پرسنل</div>
        <div class="s11-visual-sub">
          همه‌چیز شفاف، قابل برنامه‌ریزی و مطابق سیاست‌های سازمان شما
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-18-settlement.html ===

```html
<section
  class="slide"
  data-chapter="3"
  data-title="روش‌های تسویه سازمانی اوورشارژ (پیش‌پرداخت و پس‌پرداخت)">
  <div class="slide-inner">
    <!-- ── هدر اسلاید ── -->
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">فصل چهارم · انعطاف مالی و تسویه</span>
      <span class="s18-top-hint"
        >تخفیف نقدی تا ۶٪ در مدل پیش‌پرداخت یا تسویه اعتباری دوره‌ای</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      روش‌های تسویه سازمانی:
      <span class="accent-green">مدل پیش‌پرداخت</span> و
      <span class="accent-orange">مدل پس‌پرداخت</span>
    </h2>

    <!-- ── گرید دو کارت: پیش‌پرداخت vs پس‌پرداخت ── -->
    <div class="s18-grid anim-up delay-3">
      <!-- ═══ کارت پیش‌پرداخت ═══ -->
      <div class="glass-card s18-pay-card s18-card-green">
        <!-- سر کارت -->
        <div class="s18-card-head">
          <div class="s18-card-head-text">
            <h3 class="s18-card-title">مدل پیش‌پرداخت (Pre-paid)</h3>
            <span class="s18-card-sub">
              سازمان ابتدا پرداخت را انجام می‌دهد؛ سپس مزایا برای کارکنان فعال
              می‌شود
            </span>
          </div>
          <span class="s18-bonus-badge">✨ تا ۶٪ شارژ تشویقی اوانو</span>
        </div>

        <!-- باکس flow -->
        <div class="s18-flow-box s18-flow-box-green">
          <span class="s18-flow-label">
            مبلغ پرداختی سازمان:
            <strong class="s18-flow-value">۱۰۰ میلیون تومان</strong>
          </span>
          <span class="s18-flow-arrow">←</span>
          <span class="s18-flow-label">
            شارژ دریافتی پرسنل:
            <strong class="s18-flow-value-green">۱۰۶ میلیون تومان</strong>
          </span>
        </div>

        <!-- لیست مزایا -->
        <ul class="s18-list">
          <li>
            <strong>ارزش افزوده مستقیم برای بودجه سازمان:</strong>
            بهره‌مندی از حداکثر درصد شارژ تشویقی و تخفیف نقدی
          </li>
          <li>
            <strong>تضمین اعتبار خرید پرسنل:</strong>
            تخصیص بلافاصله و بدون وقفه در کیف پول پرسنل
          </li>
          <li>
            <strong>کاهش بروکراسی تسویه:</strong>
            تسویه کامل در ابتدای دوره بدون نیاز به پیگیری‌های مالی بعدی
          </li>
        </ul>
      </div>

      <!-- ═══ کارت پس‌پرداخت ═══ -->
      <div class="glass-card s18-pay-card s18-card-orange">
        <!-- سر کارت -->
        <div class="s18-card-head">
          <div class="s18-card-head-text">
            <h3 class="s18-card-title">مدل پس‌پرداخت (Post-paid)</h3>
            <span class="s18-card-sub">
              تسویه دوره‌ای بر اساس مصرف واقعی کارکنان در شبکه پذیرندگی
            </span>
          </div>
          <span class="s18-badge-orange">بدون نیاز به پیش‌پرداخت نقدی</span>
        </div>

        <!-- باکس flow (توضیحی) -->
        <div class="s18-flow-box s18-flow-box-orange">
          <span class="s18-flow-note">
            سازمان صرفاً هزینه خریدها و مصرف واقعی پرسنل را در انتهای دوره تسویه
            می‌کند.
          </span>
        </div>

        <!-- لیست مزایا -->
        <ul class="s18-list">
          <li>
            <strong>حفظ نقدینگی سازمان:</strong>
            منابع مالی سازمان در طول دوره آزاد باقی می‌ماند
          </li>
          <li>
            <strong>صورتحساب دقیق مصرف:</strong>
            ارسال گزارش تجمیعی شفاف از مبالغ مصرف‌شده به تفکیک پرسنل
          </li>
          <li>
            <strong>تضمین پرداخت:</strong>
            تسویه از طریق سازوکارهای قراردادی و تضمین‌های معتبر شرکتی
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-08-pwa-demo.html ===

```html
<section
  class="slide active"
  data-chapter="1"
  data-title="دموی تعاملی سوپراپلیکیشن اوانو و سه بالانس سازمانی">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge">دموی تعاملی سوپراپلیکیشن اوانو</span>
      <span class="slide-top-meta-hint"
        >اجرا و بررسی مستقیم سوپراپلیکیشن اوانو</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      دموی تعاملی <span class="accent-green">سوپراپلیکیشن اوانو</span>:
      <span class="accent-orange">اعتباری</span>
      <span class="headline-divider">|</span>
      <span class="text-sky">رفاهی</span>
      <span class="headline-divider">|</span>
      <span class="accent-green">نقدی</span>
    </h2>

    <div class="demo-slide-grid anim-up delay-3">
      <!-- ستون چپ: ۳ کارت بالانس -->
      <div class="demo-left-col">
        <div
          class="glass-card s8-balance-card s8-balance-card-sky"
          id="balCard-welfare">
          <div class="s8-balance-head">
            <h3 class="s8-balance-title text-sky">۱. موجودی رفاهی سازمانی</h3>
            <span class="s8-balance-badge s8-badge-sky">سرفصل‌های انتخابی</span>
          </div>
          <p class="s8-balance-text">
            شارژ رفاهی مستقیم یا تجمیعی برای خرید ارزاق، پوشاک، سفر و آموزش در
            شبکه پذیرندگان منتخب سازمان (پیش‌پرداخت با تا ۶٪ شارژ تشویقی یا
            پس‌پرداخت).
          </p>
        </div>

        <div
          class="glass-card s8-balance-card s8-balance-card-orange"
          id="balCard-credit">
          <div class="s8-balance-head">
            <h3 class="s8-balance-title text-orange">
              ۲. موجودی اعتباری (BNPL)
            </h3>
            <span class="s8-balance-badge s8-badge-orange">اقساطی ۱۲ ماهه</span>
          </div>
          <p class="s8-balance-text">
            خرید اقساطی بدون ضامن با بازپرداخت تا ۱۲ ماه و چرخه ریوالوینگ؛ شارژ
            مجدد اعتبار همزمان با پرداخت هر قسط ماهانه توسط کاربر.
          </p>
        </div>

        <div
          class="glass-card s8-balance-card s8-balance-card-green"
          id="balCard-cash">
          <div class="s8-balance-head">
            <h3 class="s8-balance-title text-green">
              ۳. موجودی نقدی (اوانو کارت)
            </h3>
            <span class="s8-balance-badge s8-badge-green">متصل به شتاب</span>
          </div>
          <p class="s8-balance-text">
            کارت نقدی عضو شبکه شتاب با همکاری بانک پارسیان (همپا)؛ امکان خرید
            حضوری، اینترنتی، کارت‌به‌کارت و مدیریت جریان نقدی پرسنل.
          </p>
        </div>
      </div>

      <!-- ستون راست: گوشی -->
      <div class="demo-wrap">
        <div class="iphone-18-pro-max">
          <div class="iphone-dynamic-island">
            <span class="island-camera"></span>
            <span class="island-sensor"></span>
          </div>
          <div class="iphone-screen-wrap">
            <iframe
              src="https://static-ebcom.mci.ir/ecm/ewano/pwa"
              class="iphone-pwa-iframe"
              title="دموی تعاملی سوپراپلیکیشن اوانو"
              allow="geolocation; microphone; camera; payment"></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-19-cash-solution.html ===

```html
<section
  class="slide"
  data-chapter="3"
  data-title="راهکار نقدی (اوانو کارت)، ظرفیت‌های همراه اول و ارزش‌آفرینی">
  <div class="slide-inner">
    <!-- ── هدر اسلاید ── -->
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل چهارم · راهکار نقدی و هم‌افزایی سازمانی</span
      >
      <span class="s19-top-hint"
        >همکاری EBCOM و بانک پارسیان (همپا) + خدمات ارتباطی همراه اول</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      راهکار نقدی <span class="accent-green">اوانو کارت</span>، ظرفیت‌های همراه
      اول و ارزش ایجادشده
    </h2>

    <!-- ── ۳ کارت بالا ── -->
    <div class="s19-top-cards anim-up delay-3">
      <!-- ═══ کارت ۱: راهکار نقدی — اوانو کارت ═══ -->
      <div class="glass-card s19-card s19-card-sky">
        <span class="eyebrow-badge sky s19-card-badge"
          >همکاری EBCOM و بانک پارسیان (همپا)</span
        >
        <h3 class="s19-card-title">راهکار نقدی؛ مبتنی بر اوانو کارت</h3>
        <ul class="s19-list">
          <li><strong>اتصال به شبکه بانکی</strong> و امکان کارت‌به‌کارت</li>
          <li>
            امکان <strong>فعال‌سازی یا غیرفعال‌سازی Cash Out</strong> متناسب با
            سیاست سازمان
          </li>
          <li>مدیریت و کنترل متمرکز نقدینگی کارکنان</li>
          <li>
            بهره‌مندی از ظرفیت‌های بانکی و <strong>مزایای مالیاتی</strong>
          </li>
        </ul>
      </div>

      <!-- ═══ کارت ۲: ظرفیت‌های همراه اول ═══ -->
      <div class="glass-card s19-card s19-card-orange">
        <span class="eyebrow-badge orange s19-card-badge"
          >باندل اختصاصی سازمانی</span
        >
        <h3 class="s19-card-title">ظرفیت‌های ارتباطی همراه اول</h3>
        <ul class="s19-list">
          <li>ارائه <strong>سیم‌کارت شخصی و سازمانی</strong></li>
          <li><strong>بسته اینترنت خانواده</strong> ویژه پرسنل</li>
          <li><strong>معافیت مکالمه</strong> درون‌سازمانی</li>
          <li>
            خدمات سازمانی پیشرفته:
            <strong>APN اختصاصی امن، MVPN، خدمات دیتاسنتری و ابری</strong>
          </li>
        </ul>
      </div>

      <!-- ═══ کارت ۳: ارزش دوگانه (Hover Reveal) ═══ -->
      <div class="glass-card s19-value-card s19-card-green">
        <span class="eyebrow-badge s19-card-badge">ارزش دوگانه B2B2C</span>
        <h3 class="s19-card-title">ارزش ایجادشده برای سازمان و کارکنان</h3>

        <div class="hover-reveal s19-val-reveal">
          <div class="s19-val-section s19-val-section-green">
            <div class="s19-val-title text-green">
              برای سازمان (HR/مالی/ارشد):
            </div>
            <div class="s19-val-bullets">
              <span>• کنترل و مدیریت یکپارچه</span>
              <span>• گزارش‌گیری و شفافیت</span>
              <span>• کاهش عملیات اجرایی</span>
              <span>• انعطاف‌پذیری و نگهداشت</span>
            </div>
          </div>
          <div class="s19-val-section s19-val-section-orange">
            <div class="s19-val-title text-orange">برای کارکنان:</div>
            <div class="s19-val-bullets">
              <span>• قدرت خرید بیشتر</span>
              <span>• انتخاب گسترده‌تر</span>
              <span>• دسترسی ساده‌تر</span>
              <span>• تجربه یکپارچه دیجیتال</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ── UX Flow (۷ مرحله) ── -->
    <div class="glass-card no-collapse s19-ux-card anim-up delay-4">
      <div class="s19-ux-title">
        <span>✨ تجربه کاربر (از اعتبار تا خرید):</span>
      </div>
      <div class="s19-ux-steps">
        <span class="ux-step-pill">۱. تخصیص اعتبار</span>
        <span class="ux-step-arrow">←</span>
        <span class="ux-step-pill">۲. مشاهده موجودی</span>
        <span class="ux-step-arrow">←</span>
        <span class="ux-step-pill">۳. انتخاب کالا/خدمت</span>
        <span class="ux-step-arrow">←</span>
        <span class="ux-step-pill">۴. انتخاب پذیرنده</span>
        <span class="ux-step-arrow">←</span>
        <span class="ux-step-pill">۵. پرداخت</span>
        <span class="ux-step-arrow">←</span>
        <span class="ux-step-pill">۶. تأیید تراکنش</span>
        <span class="ux-step-arrow">←</span>
        <span class="ux-step-pill ux-step-final">۷. مشاهده نتیجه</span>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-15-journey-5.html ===

```html
<section
  class="slide active"
  data-chapter="2"
  data-title="مسیر اعتبار (گام ۵ از ۶): روز معرفی به سازمان">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge green"
        >فصل سوم · مسیر استفاده از اعتبار سازمانی (گام ۵ از ۶)</span
      >
      <span class="slide-top-meta-formula"
        >تاریخ کلیدی دوم: روز معرفی به سازمان</span
      >
    </div>

    <!-- ریل پیشرفت ۶ مرحله‌ای -->
    <div class="journey-progress-rail anim-up delay-2">
      <div class="rail-step done" onclick="goToSlide(10)">
        <div class="rail-num">✓</div>
        <div class="rail-label">شارژ اعتبار پرسنل</div>
      </div>
      <div class="rail-step done" onclick="goToSlide(11)">
        <div class="rail-num">✓</div>
        <div class="rail-label">استفاده و خرید</div>
      </div>
      <div class="rail-step done" onclick="goToSlide(12)">
        <div class="rail-num">✓</div>
        <div class="rail-label">صدور صورتحساب و تنفس</div>
      </div>
      <div class="rail-step done" onclick="goToSlide(13)">
        <div class="rail-num">✓</div>
        <div class="rail-label">پرداخت اولین قسط</div>
      </div>
      <div class="rail-step current" onclick="goToSlide(14)">
        <div class="rail-num">۵</div>
        <div class="rail-label">روز معرفی به سازمان</div>
      </div>
      <div class="rail-step" onclick="goToSlide(15)">
        <div class="rail-num">۶</div>
        <div class="rail-label">روز تسویه سازمان</div>
      </div>
    </div>

    <div class="step-hero-panel s15-panel anim-up delay-3">
      <!-- کارت اصلی -->
      <div class="glass-card s15-main-card s15-main-card-pink">
        <div class="s15-badge-row">
          <span class="s15-step-badge">گام پنجم</span>
          <span class="s15-step-hint">مدیریت هوشمند مطالبات و اقساط معوق</span>
        </div>

        <h2 class="s15-main-title">۵. روز معرفی به سازمان و مدیریت دیرکرد</h2>

        <p class="s15-main-text">
          در صورتی که کاربر قسط ماهانه خود را در سررسید مقرر پرداخت نکند، در
          <strong>«روز معرفی به سازمان»</strong> لیست کاربران بدهکار به صورت
          شفاف و سیستمی برای واحد مالی/منابع انسانی سازمان ارسال می‌شود تا از
          محل حقوق کسر گردد.
        </p>

        <div class="s15-info-grid">
          <div class="s15-info-box s15-penalty-card">
            <h4 class="s15-info-title text-pink">
              نرخ جریمه دیرکرد روزانه: ۰.۰۱۵
            </h4>
            <p class="s15-info-text">
              به ازای هر روز دیرکرد از مبلغ بدهی، به عنوان جریمه از کاربر دریافت
              می‌شود.
            </p>
          </div>

          <div class="s15-info-box s15-neutral-card">
            <h4 class="s15-info-title">بدون دغدغه پیگیری فردی برای سازمان</h4>
            <p class="s15-info-text">
              اوانو تمامی مراحل یادآوری پیامکی به کاربر را انجام می‌دهد و تنها
              لیست نهایی کسر از حقوق را در تاریخ مشخص به سازمان ارائه می‌کند.
            </p>
          </div>
        </div>
      </div>

      <!-- ستون ویژوال -->
      <div class="glass-card step-visual-box s15-visual-box s15-visual-pink">
        <svg class="s15-visual-svg" viewBox="0 0 260 220">
          <circle
            cx="130"
            cy="110"
            r="82"
            fill="rgba(241,98,115,0.12)"
            class="svg-pulse"></circle>
          <rect
            x="75"
            y="55"
            width="110"
            height="110"
            rx="24"
            fill="#171F26"
            stroke="#F16273"
            stroke-width="3"></rect>
          <polygon
            points="130,72 95,92 165,92"
            fill="none"
            stroke="#F16273"
            stroke-width="3"
            stroke-linejoin="round"></polygon>
          <line
            x1="105"
            y1="96"
            x2="105"
            y2="132"
            stroke="#F16273"
            stroke-width="3.5"></line>
          <line
            x1="130"
            y1="96"
            x2="130"
            y2="132"
            stroke="#F16273"
            stroke-width="3.5"></line>
          <line
            x1="155"
            y1="96"
            x2="155"
            y2="132"
            stroke="#F16273"
            stroke-width="3.5"></line>
          <line
            x1="92"
            y1="138"
            x2="168"
            y2="138"
            stroke="#00D4B4"
            stroke-width="4"
            stroke-linecap="round"></line>
        </svg>
        <div class="s15-visual-title">
          با اوانو، مدیریت اعتبار کارکنان ساده‌تر است
        </div>
        <div class="s15-visual-sub">
          همه چیز شفاف، قابل برنامه‌ریزی و مطابق سیاست‌های سازمان شما
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-14-journey-4.html ===

```html
<section
  class="slide active"
  data-chapter="2"
  data-title="مسیر اعتبار (گام ۴ از ۶): پرداخت اولین قسط و دوره ۱۲ ماهه ریوالوینگ">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل سوم · مسیر استفاده از اعتبار سازمانی (گام ۴ از ۶)</span
      >
      <span class="slide-top-meta-formula"
        >قابلیت منحصربه‌فرد ریوالوینگ (شارژ مجدد پس از هر قسط)</span
      >
    </div>

    <!-- ریل پیشرفت ۶ مرحله‌ای -->
    <div class="journey-progress-rail anim-up delay-2">
      <div class="rail-step done" onclick="goToSlide(10)">
        <div class="rail-num">✓</div>
        <div class="rail-label">شارژ اعتبار پرسنل</div>
      </div>
      <div class="rail-step done" onclick="goToSlide(11)">
        <div class="rail-num">✓</div>
        <div class="rail-label">استفاده و خرید</div>
      </div>
      <div class="rail-step done" onclick="goToSlide(12)">
        <div class="rail-num">✓</div>
        <div class="rail-label">صدور صورتحساب و تنفس</div>
      </div>
      <div class="rail-step current" onclick="goToSlide(13)">
        <div class="rail-num">۴</div>
        <div class="rail-label">پرداخت اولین قسط</div>
      </div>
      <div class="rail-step" onclick="goToSlide(14)">
        <div class="rail-num">۵</div>
        <div class="rail-label">روز معرفی به سازمان</div>
      </div>
      <div class="rail-step" onclick="goToSlide(15)">
        <div class="rail-num">۶</div>
        <div class="rail-label">روز تسویه سازمان</div>
      </div>
    </div>

    <div class="step-hero-panel s14-panel anim-up delay-3">
      <!-- کارت اصلی -->
      <div class="glass-card s14-main-card s14-main-card-green">
        <div class="s14-badge-row">
          <span class="s14-step-badge">گام چهارم</span>
          <span class="s14-step-hint">۴ روز پس از اتمام دوره تنفس</span>
        </div>

        <h2 class="s14-main-title">
          ۴. مهلت پرداخت اولین قسط و
          <span class="accent-green">دوره ۱۲ ماهه ریوالوینگ</span>
        </h2>

        <p class="s14-main-text">
          کاربر <strong>۴ روز پس از اتمام دوره تنفس</strong> فرصت دارد اولین قسط
          خود را پرداخت کند. با آغاز دوره بازپرداخت ۱۲ ماهه، پس از پرداخت هر
          قسط،
          <strong
            >معادل مبلغ قسط پرداخت‌شده بلافاصله به کیف پول اعتباری کاربر
            بازمی‌گردد (Revolving)</strong
          >
          و برای خریدهای بعدی قابل استفاده است.
        </p>

        <div class="s14-info-grid">
          <div class="s14-info-box s14-info-green">
            <div class="s14-info-title text-green">ویژگی‌های دوره اقساط:</div>
            <ul class="s14-list">
              <li>• مدت بازپرداخت <strong>۱۲ ماهه</strong></li>
              <li>• پرداخت اولین قسط ۴ روز پس از دوره تنفس</li>
              <li>• ریوالوینگ مبلغ هر قسط پس از پرداخت</li>
              <li>• ادامه امکان استفاده مستمر از اعتبار</li>
            </ul>
          </div>

          <div class="s14-info-box s14-info-orange">
            <div class="s14-info-title text-orange">
              مزیت چرخه ریوالوینگ برای کارمند:
            </div>
            <p class="s14-info-text">
              کارمند نیاز نیست ۱۲ ماه صبر کند تا کل وام تسویه شود؛ با هر قسط،
              قدرت خرید او مجدداً شارژ می‌شود.
            </p>
          </div>
        </div>
      </div>

      <!-- ستون ویژوال -->
      <div class="glass-card step-visual-box s14-visual-box">
        <svg class="s14-visual-svg" viewBox="0 0 320 280">
          <!-- حلقه‌های ریوالوینگ -->
          <circle
            cx="160"
            cy="140"
            r="114"
            fill="none"
            stroke="rgba(0,212,180,0.3)"
            stroke-width="9"
            stroke-dasharray="24 12"
            class="svg-flow-line"></circle>
          <circle
            cx="160"
            cy="140"
            r="78"
            fill="#171F26"
            stroke="#00D4B4"
            stroke-width="3.2"></circle>

          <text
            x="160"
            y="114"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#00D4B4"
            font-size="24"
            font-weight="900">
            ۱۲ ماهه
          </text>
          <text
            x="160"
            y="146"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#FFFFFF"
            font-size="20"
            font-weight="900">
            ریوالوینگ
          </text>
          <text
            x="160"
            y="174"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#CBD5E1"
            font-size="16"
            font-weight="700">
            (Revolving)
          </text>
        </svg>
        <div class="s14-visual-title">
          بازگشت آنی اعتبار پس از پرداخت هر قسط
        </div>
        <div class="s14-visual-sub">حفظ دائمی قدرت خرید کارکنان در طول سال</div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-09-features.html ===

```html
<section
  class="slide active"
  data-chapter="1"
  data-title="ویژگی‌های کلیدی اعتبار سازمانی اوانو">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل دوم · مزیت‌های رقابتی اعتبار سازمانی</span
      >
      <span class="slide-top-meta-hint"
        >طراحی‌شده بر اساس نیازهای واقعی مدیران منابع انسانی و مالی</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      ویژگی‌های کلیدی
      <span class="accent-green">اعتبار سازمانی</span> اوانو و EBCOM
    </h2>

    <div class="s9-features-grid anim-up delay-3">
      <div class="s9-feature-card s9-card-green">
        <div class="s9-icon">🏦</div>
        <h3 class="s9-title">بدون نیاز به اعتبارسنجی بانکی</h3>
        <p class="s9-text">
          حذف کامل بروکراسی‌های سنتی بانکی، ضامن و چک؛ تخصیص اعتبار صرفاً بر
          مبنای معرفی و ضمانت کسر از حقوق سازمان.
        </p>
      </div>

      <div class="s9-feature-card s9-card-orange">
        <div class="s9-icon">💎</div>
        <h3 class="s9-title">تأمین سرمایه از طریق همراه اول</h3>
        <p class="s9-text">
          پشتوانه مالی قدرتمند گروه همراه اول و EBCOM برای تأمین پایدار خطوط
          اعتباری سازمان‌های بزرگ بدون بار نقدینگی اولیه بر دوش سازمان.
        </p>
      </div>

      <div class="s9-feature-card s9-card-sky">
        <div class="s9-icon">⚙️</div>
        <h3 class="s9-title">تخصیص بر اساس سیاست‌های سازمان</h3>
        <p class="s9-text">
          تعیین سقف و ضوابط اعتبار برای هر گروه از کارکنان بر مبنای
          <strong>سنوات خدمت، میزان حقوق و جایگاه سازمانی</strong>.
        </p>
      </div>

      <div class="s9-feature-card s9-card-pastel">
        <div class="s9-icon">🎛️</div>
        <h3 class="s9-title">امکان کنترل و مدیریت مصرف اعتبار</h3>
        <p class="s9-text">
          مدیریت کامل سقف‌ها، دسته‌بندی‌های مجاز و پایش لحظه‌ای میزان اعتبار
          تخصیص‌یافته و مصرف‌شده توسط پرسنل.
        </p>
      </div>

      <div class="s9-feature-card s9-card-yellow">
        <div class="s9-icon">🛍️</div>
        <h3 class="s9-title">استفاده در شبکه گسترده پذیرندگان</h3>
        <p class="s9-text">
          امکان خرید آسان از ۹٬۴۱۵ پذیرنده آنلاین و حضوری (بیش از ۱۰٬۴۷۲ شعبه در
          سراسر کشور) با اسکن QR یا درگاه پرداخت.
        </p>
      </div>

      <div class="s9-feature-card s9-card-purple">
        <div class="s9-icon">📊</div>
        <h3 class="s9-title">شفافیت و گزارش‌پذیری تراکنش‌ها</h3>
        <p class="s9-text">
          دسترسی آنی مدیران مالی و منابع انسانی به گزارش‌های دقیق مصرف،
          صورتحساب‌های ماهانه و وضعیت تسویه کارکنان.
        </p>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-01-hero.html ===

```html
<section class="slide active" data-chapter="0" data-title="صفحه عنوان: راهکارهای سازمانی و اعتباری اوانو">
  <div class="slide-inner">
    <div class="hero-grid grid-2-asym">

      <!-- ستون متن -->
      <div class="hero-text-col flex-col flex-gap-20">
        <div class="anim-up delay-1 flex flex-gap-10 flex-wrap">
          <span class="eyebrow-badge">ارائه حضوری راهکارهای سازمانی B2B</span>
          <span class="eyebrow-badge orange">ویژه مدیران ارشد، منابع انسانی و مالی</span>
        </div>

        <h1 class="slide-headline hero-headline anim-up delay-2">
          اعتبار و خدمات رفاهی کارکنان،<br>
          <span class="accent-green">متناسب با نیاز سازمان شما</span>
        </h1>

        <p class="slide-subtitle anim-up delay-3">
          با راهکارهای سازمانی <strong>اوانو</strong> و زیرساخت مالی <strong>همراه کسب‌وکارهای هوشمند (EBCOM)</strong>، مجموعه‌ای یکپارچه از خدمات اعتباری، رفاهی و نقدی را در اختیار کارکنان خود قرار دهید و مدیریت مزایای سازمانی را ساده، شفاف و هوشمند پیش ببرید.
        </p>

        <div class="hero-stats grid-3 anim-up delay-4">
          <div class="glass-card hero-stat-card border-right-green">
            <div class="hero-stat-value text-green">+۲۸ میلیون</div>
            <p class="hero-stat-label">کاربر فعال در اکوسیستم اوانو</p>
          </div>
          <div class="glass-card hero-stat-card border-right-orange">
            <div class="hero-stat-value text-orange">۹٬۴۱۵ مرچنت</div>
            <p class="hero-stat-label">۱۰٬۴۷۲ نقطه و شعبه پذیرندگی</p>
          </div>
          <div class="glass-card hero-stat-card border-right-sky">
            <div class="hero-stat-value text-sky">+۲۰ همت</div>
            <p class="hero-stat-label">حجم خرید و ۱۵ میلیون تراکنش ماهانه</p>
          </div>
        </div>

        <div class="hero-cta-row anim-up delay-5">
          <button class="nav-arrow-btn hero-btn-primary" onclick="nextSlide()">
            <span>شروع پرزنتیشن</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <line x1="19" y1="12" x2="5" y2="12"/>
              <polyline points="12 19 5 12 12 5"/>
            </svg>
          </button>
          <button class="nav-arrow-btn hero-btn-secondary" onclick="goToSlide(10)">
            <span>مشاهده مسیر ۶ مرحله‌ای اعتبار</span>
          </button>
        </div>
      </div>

      <!-- ستون کارت‌های ۳D -->
      <div class="hero-cards-stage anim-up delay-3">
        <div class="ewano-3d-card card-welfare">
          <div class="card-top-row">
            <div class="card-chip"></div>
            <span class="text-xs font-black rounded-pill card-badge">WELFARE BALANCE</span>
          </div>
          <div>
            <div class="card-balance-title">موجودی رفاهی سازمانی</div>
            <div class="card-balance-sub">تخصیص مزایا در سرفصل‌های معیشتی، سفر و بیمه</div>
          </div>
          <div class="flex-between text-xs font-black">
            <span>شارژ تشویقی تا ۶٪</span>
            <span>ewano.app</span>
          </div>
        </div>

        <div class="ewano-3d-card card-credit">
          <div class="card-top-row">
            <div class="card-chip"></div>
            <span class="text-xs font-black rounded-pill card-badge">CORPORATE CREDIT</span>
          </div>
          <div>
            <div class="card-balance-title">موجودی اعتبار اوانو</div>
            <div class="card-balance-sub">خرید اقساطی ۴ تا ۲۴ ماهه با ضمانت کسر از حقوق (ریوالوینگ)</div>
          </div>
          <div class="flex-between text-xs font-black">
            <span>بدون اعتبارسنجی بانکی</span>
            <span>EBCOM</span>
          </div>
        </div>

        <div class="ewano-3d-card card-cash">
          <div class="card-top-row">
            <div class="card-chip"></div>
            <span class="text-xs font-black rounded-pill card-badge">CASH & GIFT CARD</span>
          </div>
          <div>
            <div class="card-balance-title">موجودی نقدی و گیفت‌کارت</div>
            <div class="card-balance-sub">شارژ مستقیم کیف پول نقدی و ووچرکارت‌های سازمانی</div>
          </div>
          <div class="flex-between text-xs font-black">
            <span>کارت به کارت و پرداخت آنی</span>
            <span>EWANO WALLET</span>
          </div>
        </div>

        <div class="ewano-3d-card card-debit-black" id="debitCardFlipper" onclick="toggleDebitCardFlip(this)" title="برای مشاهده پشت کارت کلیک کنید">
          <div class="debit-flipper-inner">
            <div class="debit-side debit-front">
              <img src="assets/images/cards/debit-front.png" alt="روی دبیت کارت اوانو" class="debit-img">
            </div>
            <div class="debit-side debit-back">
              <img src="assets/images/cards/debit-back.png" alt="پشت دبیت کارت اوانو" class="debit-img">
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
```

=== ./slides/slide-13-journey-3.html ===

```html
<section
  class="slide active"
  data-chapter="2"
  data-title="مسیر اعتبار (گام ۳ از ۶): صدور صورتحساب و دوره تنفس ۳ روزه">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل سوم · مسیر استفاده از اعتبار سازمانی (گام ۳ از ۶)</span
      >
      <span class="slide-top-meta-formula s13-hint-purple"
        >نقطه انعطاف‌پذیری: انتخاب بین تسویه نقدی یا اقساطی</span
      >
    </div>

    <!-- ریل پیشرفت ۶ مرحله‌ای -->
    <div class="journey-progress-rail anim-up delay-2">
      <div class="rail-step done" onclick="goToSlide(10)">
        <div class="rail-num">✓</div>
        <div class="rail-label">شارژ اعتبار پرسنل</div>
      </div>
      <div class="rail-step done" onclick="goToSlide(11)">
        <div class="rail-num">✓</div>
        <div class="rail-label">استفاده و خرید</div>
      </div>
      <div class="rail-step current" onclick="goToSlide(12)">
        <div class="rail-num">۳</div>
        <div class="rail-label">صدور صورتحساب و تنفس</div>
      </div>
      <div class="rail-step" onclick="goToSlide(13)">
        <div class="rail-num">۴</div>
        <div class="rail-label">پرداخت اولین قسط</div>
      </div>
      <div class="rail-step" onclick="goToSlide(14)">
        <div class="rail-num">۵</div>
        <div class="rail-label">روز معرفی به سازمان</div>
      </div>
      <div class="rail-step" onclick="goToSlide(15)">
        <div class="rail-num">۶</div>
        <div class="rail-label">روز تسویه سازمان</div>
      </div>
    </div>

    <div class="step-hero-panel s13-panel anim-up delay-3">
      <!-- کارت اصلی -->
      <div class="glass-card s13-main-card s13-main-card-purple">
        <div class="s13-badge-row">
          <span class="s13-step-badge">گام سوم + دوره تنفس ۳ روزه</span>
          <span class="s13-step-hint">تاریخ کلیدی اول: روز صدور صورتحساب</span>
        </div>

        <h2 class="s13-main-title">
          ۳. صدور صورتحساب و
          <span class="accent-green">دوره تنفس ۳ روزه</span>
        </h2>

        <p class="s13-main-text">
          در روز صدور صورتحساب، کاربر جزئیات خریدهای ماهانه خود را مشاهده می‌کند
          و <strong>۳ روز دوره تنفس</strong> فرصت دارد تا روش بازپرداخت خود را
          بین <strong>تسویه نقدی (بدون کارمزد)</strong> یا
          <strong>ورود به دوره اقساط ۱۲ ماهه</strong> انتخاب کند:
        </p>

        <!-- دو گزینه انشعابی -->
        <div class="s13-options-grid">
          <div class="s13-option s13-option-cash">
            <div class="s13-option-title text-green">گزینه اول: تسویه نقدی</div>
            <ul class="s13-list">
              <li>
                ✓ پرداخت کل مبلغ صورتحساب <strong>بدون هیچ کارمزدی</strong>
              </li>
              <li>✓ خروج سریع از طرح و تسویه کامل</li>
              <li>✓ آزادی در استفاده مجدد بلافاصله از تمام اعتبار</li>
            </ul>
          </div>

          <div class="s13-option s13-option-installment">
            <div class="s13-option-title text-sky">
              گزینه دوم: انتخاب اقساطی
            </div>
            <ul class="s13-list">
              <li>✓ در صورت انتخاب اقساطی (یا عدم انتخاب در ۳ روز)</li>
              <li>✓ ورود خودکار به فرآیند تقسیط <strong>۱۲ ماهه</strong></li>
              <li>✓ ادامه امکان استفاده از باقیمانده اعتبار</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- ستون ویژوال -->
      <div class="glass-card step-visual-box s13-visual-box s13-visual-purple">
        <svg class="s13-visual-svg" viewBox="0 0 380 250">
          <!-- جعبه صورتحساب -->
          <rect
            x="105"
            y="12"
            width="170"
            height="56"
            rx="16"
            fill="#1F2933"
            stroke="#A78BFA"
            stroke-width="2.5"></rect>
          <text
            x="190"
            y="36"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#FFFFFF"
            font-size="14"
            font-weight="900">
            صدور صورتحساب
          </text>
          <text
            x="190"
            y="54"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#A78BFA"
            font-size="11.5"
            font-weight="800">
            ⏱ دوره تنفس: ۳ روز
          </text>

          <!-- مسیرهای انشعاب -->
          <path
            d="M190 68 L190 92 L95 92 L95 125"
            fill="none"
            stroke="#00D4B4"
            stroke-width="2.8"
            stroke-dasharray="5 3"
            class="svg-flow-line"></path>
          <path
            d="M190 68 L190 92 L285 92 L285 125"
            fill="none"
            stroke="#0093DD"
            stroke-width="2.8"
            stroke-dasharray="5 3"
            class="svg-flow-line"></path>

          <!-- شاخه چپ: تسویه نقدی -->
          <rect
            x="15"
            y="125"
            width="160"
            height="95"
            rx="18"
            fill="rgba(0,212,180,0.15)"
            stroke="#00D4B4"
            stroke-width="2.2"></rect>
          <text
            x="95"
            y="152"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#00D4B4"
            font-size="14.5"
            font-weight="900">
            تسویه نقدی
          </text>
          <text
            x="95"
            y="174"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#FFFFFF"
            font-size="11.5"
            font-weight="800">
            بدون هیچ کارمزدی
          </text>
          <text
            x="95"
            y="194"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#CBD5E1"
            font-size="10.5">
            خروج سریع و شارژ مجدد
          </text>

          <!-- شاخه راست: انتخاب اقساطی -->
          <rect
            x="205"
            y="125"
            width="160"
            height="95"
            rx="18"
            fill="rgba(0,147,221,0.15)"
            stroke="#0093DD"
            stroke-width="2.2"></rect>
          <text
            x="285"
            y="152"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#0093DD"
            font-size="14.5"
            font-weight="900">
            انتخاب اقساطی
          </text>
          <text
            x="285"
            y="174"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#FFFFFF"
            font-size="11.5"
            font-weight="800">
            ورود به دوره ۱۲ ماهه
          </text>
          <text
            x="285"
            y="194"
            text-anchor="middle"
            dominant-baseline="middle"
            fill="#CBD5E1"
            font-size="10.5">
            تقسیط خودکار بدهی
          </text>
        </svg>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-12-journey-2.html ===

```html
<section
  class="slide active"
  data-chapter="2"
  data-title="مسیر اعتبار (گام ۲ از ۶): استفاده از اعتبار و خرید">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل سوم · مسیر استفاده از اعتبار سازمانی (گام ۲ از ۶)</span
      >
      <span class="slide-top-meta-formula">آزادی انتخاب در سراسر کشور</span>
    </div>

    <!-- ریل پیشرفت ۶ مرحله‌ای -->
    <div class="journey-progress-rail anim-up delay-2">
      <div class="rail-step done" onclick="goToSlide(10)">
        <div class="rail-num">✓</div>
        <div class="rail-label">شارژ اعتبار پرسنل</div>
      </div>
      <div class="rail-step current" onclick="goToSlide(11)">
        <div class="rail-num">۲</div>
        <div class="rail-label">استفاده و خرید</div>
      </div>
      <div class="rail-step" onclick="goToSlide(12)">
        <div class="rail-num">۳</div>
        <div class="rail-label">صدور صورتحساب و تنفس</div>
      </div>
      <div class="rail-step" onclick="goToSlide(13)">
        <div class="rail-num">۴</div>
        <div class="rail-label">پرداخت اولین قسط</div>
      </div>
      <div class="rail-step" onclick="goToSlide(14)">
        <div class="rail-num">۵</div>
        <div class="rail-label">روز معرفی به سازمان</div>
      </div>
      <div class="rail-step" onclick="goToSlide(15)">
        <div class="rail-num">۶</div>
        <div class="rail-label">روز تسویه سازمان</div>
      </div>
    </div>

    <div class="step-hero-panel s12-panel anim-up delay-3">
      <!-- کارت اصلی -->
      <div class="glass-card s12-main-card s12-main-card-sky">
        <div class="s12-badge-row">
          <span class="s12-step-badge">گام دوم</span>
          <span class="s12-step-hint">تجربه خرید بی‌مرز آنلاین و حضوری</span>
        </div>

        <h2 class="s12-main-title">
          ۲. استفاده از اعتبار و خرید از شبکه پذیرندگان
        </h2>

        <p class="s12-main-text">
          کارکنان پس از شارژ کیف پول اعتباری، می‌توانند در هر زمان از شبانه‌روز
          از
          <strong>شبکه گسترده پذیرندگان آنلاین و حضوری اوانو</strong>
          (شامل ۵٬۴۳۸ فروشگاه اینترنتی و ۱۰٬۴۷۲ شعبه حضوری در سراسر کشور) خرید
          خود را انجام دهند.
        </p>

        <div class="s12-tips-grid">
          <div class="s12-tip-box s12-tip-sky">
            <div class="s12-tip-title">
              🛒 خرید آنلاین از وب‌سایت‌ها و داخل اپ
            </div>
            <div class="s12-tip-sub">
              انتخاب درگاه اوانو در دیجی‌کالا، اسنپ، تکنولایف، اُکالا، طلاسی
              و...
            </div>
          </div>
          <div class="s12-tip-box s12-tip-green">
            <div class="s12-tip-title">📱 خرید حضوری با اسکن بارکد QR</div>
            <div class="s12-tip-sub">
              پرداخت آنی در افق کوروش، دیلی‌مارکت، رفاه، هایپراستار، ایران‌مال
              و...
            </div>
          </div>
        </div>
      </div>

      <!-- ستون ویژوال -->
      <div class="glass-card step-visual-box s12-visual-box s12-visual-sky">
        <svg class="s12-visual-svg" viewBox="0 0 260 220">
          <circle
            cx="130"
            cy="110"
            r="82"
            fill="rgba(0,147,221,0.14)"
            class="svg-pulse"></circle>
          <rect
            x="75"
            y="55"
            width="110"
            height="110"
            rx="24"
            fill="#171F26"
            stroke="#0093DD"
            stroke-width="3"></rect>
          <circle cx="112" cy="142" r="6" fill="#00D4B4"></circle>
          <circle cx="148" cy="142" r="6" fill="#00D4B4"></circle>
          <path
            d="M92 80h14l10 44h38l8-30H104"
            fill="none"
            stroke="#0093DD"
            stroke-width="3.5"
            stroke-linecap="round"
            stroke-linejoin="round"></path>
        </svg>
        <div class="s12-visual-title">
          خرید از شبکه پذیرندگان آنلاین و حضوری
        </div>
        <div class="s12-visual-sub">
          ۹٬۴۱۵ مرچنت فعال و ۱۰٬۴۷۲ نقطه فروش در سراسر کشور
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-10-calculator.html ===

```html
<section
  class="slide active"
  data-chapter="1"
  data-title="ماشین حساب اعتبار خرید و نحوه محاسبه اقساط">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge"
        >فصل دوم · شبیه‌ساز مالی و محاسبه اقساط اعتبار</span
      >
      <span class="slide-top-meta-formula"
        >فرمول رسمی: مبلغ هر قسط = (اصل اعتبار ÷ تعداد اقساط) + (اصل اعتبار ×
        درصد کارمزد)</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      ماشین حساب <span class="accent-green">اعتبار خرید</span> و محاسبه اقساط
      ماهانه
    </h2>

    <div class="calc-grid-layout s10-calc-grid anim-up delay-3">
      <!-- ماشین حساب -->
      <div class="calc no-collapse" id="creditCalc">
        <div class="calc-inputs">
          <!-- ردیف ۱: مبلغ اعتبار -->
          <div class="calc-row">
            <div class="calc-row-head">
              <label for="calcAmount">اصل مبلغ اعتبار مصرفی (تومان)</label>
              <output id="calcAmountOut" for="calcAmount" class="calc-amount"
                >۱۰۰٬۰۰۰٬۰۰۰<small>تومان</small></output
              >
            </div>
            <div class="calc-track" style="--f: 0.4444444444444444">
              <div class="calc-line" aria-hidden="true"><i></i></div>
              <div class="calc-ticks" aria-hidden="true">
                <i class="on"><b>۲۰</b></i
                ><i class="on"><b>۴۰</b></i
                ><i class="on"><b>۶۰</b></i
                ><i class="on"><b>۸۰</b></i
                ><i class="cur"><b>۱۰۰</b></i
                ><i><b>۱۲۰</b></i
                ><i><b>۱۴۰</b></i
                ><i><b>۱۶۰</b></i
                ><i><b>۱۸۰</b></i
                ><i><b>۲۰۰</b></i>
              </div>
              <span class="calc-pin" aria-hidden="true">
                <svg viewBox="0 0 24 28">
                  <path
                    fill="currentColor"
                    d="M12 1C6.2 1 1.8 5.4 1.8 11c0 7.3 8.7 14.9 9.5 15.6.4.3 1 .3 1.4 0 .8-.7 9.5-8.3 9.5-15.6C22.2 5.4 17.8 1 12 1Z"></path>
                  <circle cx="12" cy="11" r="4.2" fill="#fff"></circle>
                </svg>
              </span>
              <input
                type="range"
                id="calcAmount"
                class="calc-range"
                min="20000000"
                max="200000000"
                step="20000000"
                value="100000000" />
            </div>
          </div>

          <!-- ردیف ۲: تعداد اقساط -->
          <div class="calc-row">
            <div class="calc-row-head">
              <label for="calcCountIdx"
                >تعداد اقساط (۴، ۶، ۱۲، ۱۸ یا ۲۴ ماهه)</label
              >
              <output id="calcCountOut" for="calcCountIdx" class="calc-amount"
                >۱۲<small>قسط ماهانه</small></output
              >
            </div>
            <div class="calc-track" style="--f: 0.5">
              <div class="calc-line" aria-hidden="true"><i></i></div>
              <div class="calc-ticks" aria-hidden="true">
                <i class="on"><b>۴ ماهه</b></i
                ><i class="on"><b>۶ ماهه</b></i
                ><i class="cur"><b>۱۲ ماهه</b></i
                ><i><b>۱۸ ماهه</b></i
                ><i><b>۲۴ ماهه</b></i>
              </div>
              <span class="calc-pin" aria-hidden="true">
                <svg viewBox="0 0 24 28">
                  <path
                    fill="currentColor"
                    d="M12 1C6.2 1 1.8 5.4 1.8 11c0 7.3 8.7 14.9 9.5 15.6.4.3 1 .3 1.4 0 .8-.7 9.5-8.3 9.5-15.6C22.2 5.4 17.8 1 12 1Z"></path>
                  <circle cx="12" cy="11" r="4.2" fill="#fff"></circle>
                </svg>
              </span>
              <input
                type="range"
                id="calcCountIdx"
                class="calc-range"
                min="0"
                max="4"
                step="1"
                value="2" />
            </div>
          </div>

          <!-- ردیف ۳: درصد کارمزد -->
          <div class="calc-row">
            <div class="calc-row-head">
              <label for="calcFeeRate"
                >درصد کارمزد ماهانه (متغیر بر اساس توافق سازمان)</label
              >
              <div class="s10-fee-wrap">
                <input
                  type="number"
                  id="calcFeeInput"
                  class="s10-fee-input"
                  min="0"
                  max="5"
                  step="0.1"
                  value="1.9"
                  dir="ltr" />
                <output
                  id="calcFeeOut"
                  for="calcFeeRate"
                  class="calc-amount text-orange"
                  >۱٫۹<small>٪ ماهانه</small></output
                >
              </div>
            </div>
            <div class="calc-track" style="--f: 0.475">
              <div class="calc-line" aria-hidden="true"><i></i></div>
              <div class="calc-ticks" aria-hidden="true">
                <i class="on"><b>۰٪</b></i
                ><i class="on"><b>۱٪</b></i
                ><i class="cur"><b>۱٫۹٪</b></i
                ><i><b>۳٪</b></i
                ><i><b>۴٪</b></i>
              </div>
              <span class="calc-pin" aria-hidden="true">
                <svg viewBox="0 0 24 28">
                  <path
                    fill="currentColor"
                    d="M12 1C6.2 1 1.8 5.4 1.8 11c0 7.3 8.7 14.9 9.5 15.6.4.3 1 .3 1.4 0 .8-.7 9.5-8.3 9.5-15.6C22.2 5.4 17.8 1 12 1Z"></path>
                  <circle cx="12" cy="11" r="4.2" fill="#fff"></circle>
                </svg>
              </span>
              <input
                type="range"
                id="calcFeeRate"
                class="calc-range"
                min="0"
                max="4"
                step="0.1"
                value="1.9" />
            </div>
          </div>
        </div>

        <!-- نتیجه -->
        <div class="calc-result" aria-live="polite">
          <div>
            <span class="calc-res-lbl">مبلغ هر قسط ماهانه</span>
            <div class="calc-res-main">
              <b id="calcInst">۱۰٬۲۳۳٬۳۳۳</b><span>تومان در ماه</span>
            </div>
            <div id="calcFormulaText" class="s10-formula-text">
              (100,000,000 ÷ 12) + (100,000,000 × 1.9%) = 10,233,333
            </div>
          </div>
          <dl class="calc-res-list s10-res-list">
            <div>
              <dt>سهم اصل اعتبار در هر قسط</dt>
              <dd id="calcResBase">۸٬۳۳۳٬۳۳۳ تومان</dd>
            </div>
            <div>
              <dt>مبلغ کارمزد هر قسط</dt>
              <dd id="calcResFee" class="text-orange">۱٬۹۰۰٬۰۰۰ تومان</dd>
            </div>
            <div>
              <dt>تعداد و نرخ کارمزد</dt>
              <dd id="calcResCount">۱۲ ماهه · کارمزد ۱٫۹٪</dd>
            </div>
            <div>
              <dt>مجموع کل بازپرداخت</dt>
              <dd id="calcResTotal" class="text-green">۱۲۲٬۸۰۰٬۰۰۰ تومان</dd>
            </div>
          </dl>
        </div>
      </div>

      <!-- ستون کنار: ۳ کارت توضیح -->
      <div class="calc-side-stack s10-side-stack">
        <div class="glass-card calc-side-card s10-side-card s10-side-green">
          <span class="eyebrow-badge s10-side-badge"
            >فرمول محاسبه اقساط اعتبار</span
          >
          <h3 class="s10-side-title">ساختار شفاف محاسبه هر قسط</h3>
          <p class="s10-side-text">
            مبلغ هر قسط از مجموع
            <strong>«اصل مبلغ اعتبار تقسیم بر تعداد اقساط»</strong> به علاوه
            <strong>«درصد کارمزد ضربدر اصل مبلغ اعتبار مصرفی»</strong>
            محاسبه می‌شود:
            <br />
            <strong class="s10-side-formula"
              >مبلغ هر قسط = (اصل اعتبار ÷ تعداد اقساط) + (اصل اعتبار × درصد
              کارمزد)</strong
            >
          </p>
        </div>

        <div class="glass-card calc-side-card s10-side-card s10-side-orange">
          <span class="eyebrow-badge orange s10-side-badge"
            >مثال مرجع (کلیک برای بارگذاری)</span
          >
          <h3 class="s10-side-title">
            خرید اعتباری ۱۰۰ میلیون تومانی (۱۲ ماهه با کارمزد ۱.۹٪)
          </h3>
          <p class="s10-side-text">
            • سهم اصل در هر قسط: <strong>۸٬۳۳۳٬۳۳۳ تومان</strong> (۱۰۰ میلیون ÷
            ۱۲)<br />
            • کارمزد هر قسط: <strong>۱٬۹۰۰٬۰۰۰ تومان</strong> (۱۰۰ میلیون ×
            ۱.۹٪)<br />
            • <strong>مبلغ نهایی هر قسط: ۱۰٬۲۳۳٬۳۳۳ تومان</strong>
          </p>
        </div>

        <div class="glass-card calc-side-card s10-side-card s10-side-sky">
          <span class="eyebrow-badge sky s10-side-badge"
            >انعطاف در دوره‌های بازپرداخت</span
          >
          <h3 class="s10-side-title">
            تعداد اقساط ۴، ۶، ۱۲، ۱۸ و ۲۴ ماهه + کارمزد متغیر
          </h3>
          <p class="s10-side-text">
            تعداد اقساط در ۵ بازه استاندارد (۴، ۶، ۱۲، ۱۸ و ۲۴ ماه) قابل انتخاب
            است و درصد کارمزد نیز بر اساس تفاهم‌نامه و مدل همکاری هر سازمان به
            صورت متغیر تنظیم می‌گردد.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
```

=== ./slides/slide-06-challenges.html ===

```html
<section
  class="slide active"
  data-chapter="1"
  data-title="چالش‌های مدیریت مزایا و خدمات رفاهی کارکنان">
  <div class="slide-inner">
    <div class="slide-top-meta anim-up delay-1">
      <span class="eyebrow-badge orange">فصل دوم · مسئله‌شناسی سازمانی</span>
      <span class="slide-top-meta-hint"
        >چرا سازمان‌ها به یک زیرساخت متمرکز نیاز دارند؟</span
      >
    </div>

    <h2 class="slide-headline anim-up delay-2">
      مدیریت خدمات و مزایای کارکنان
      <span class="accent-orange">همیشه ساده نیست!</span>
    </h2>

    <p class="slide-subtitle anim-up delay-2">
      با افزایش تعداد کارکنان و تنوع نیازهای آن‌ها، مدیریت خدمات رفاهی و اعتباری
      به فرآیندی پیچیده و زمان‌بر تبدیل می‌شود. ۵ چالش اصلی سازمان‌ها و پاسخ
      یکپارچه اوانو:
    </p>

    <div class="s6-challenges-grid anim-up delay-3">
      <div class="s6-challenge-card">
        <div class="s6-num">۰۱</div>
        <h4 class="s6-challenge-title">خدمات و مزایای پراکنده</h4>
        <p class="s6-challenge-text">
          مدیریت چندین خدمت و ارائه‌دهنده مختلف، فرآیندهای اجرایی سازمان را
          پیچیده و فرسایشی می‌کند.
        </p>
        <div class="s6-solution">
          <span class="s6-check">✓</span>
          <span>راهکار اوانو: تجمیع در یک پلتفرم واحد</span>
        </div>
      </div>

      <div class="s6-challenge-card">
        <div class="s6-num">۰۲</div>
        <h4 class="s6-challenge-title">فرآیندهای زمان‌بر اجرایی</h4>
        <p class="s6-challenge-text">
          ارائه، توزیع و پیگیری مزایا برای تعداد بالای پرسنل نیازمند زمان و
          منابع انسانی قابل‌توجهی است.
        </p>
        <div class="s6-solution">
          <span class="s6-check">✓</span>
          <span>راهکار اوانو: تخصیص آنی و خودکار</span>
        </div>
      </div>

      <div class="s6-challenge-card">
        <div class="s6-num">۰۳</div>
        <h4 class="s6-challenge-title">کنترل و مدیریت هزینه‌ها</h4>
        <p class="s6-challenge-text">
          مدیریت بودجه و اعتبار اختصاص‌یافته به کارکنان و نظارت دقیق بر نحوه
          مصرف آن چالش‌برانگیز است.
        </p>
        <div class="s6-solution">
          <span class="s6-check">✓</span>
          <span>راهکار اوانو: داشبورد گزارش‌گیری شفاف</span>
        </div>
      </div>

      <div class="s6-challenge-card">
        <div class="s6-num">۰۴</div>
        <h4 class="s6-challenge-title">نیازهای متفاوت کارکنان</h4>
        <p class="s6-challenge-text">
          کارکنان در گروه‌های مختلف سازمانی ترجیحات متفاوتی دارند و یک بسته ثابت
          پاسخگوی همه نیست.
        </p>
        <div class="s6-solution">
          <span class="s6-check">✓</span>
          <span>راهکار اوانو: تخصیص بر اساس سیاست سازمان</span>
        </div>
      </div>

      <div class="s6-challenge-card">
        <div class="s6-num">۰۵</div>
        <h4 class="s6-challenge-title">انتظار مزایای متنوع‌تر</h4>
        <p class="s6-challenge-text">
          کارکنان به دنبال آزادی انتخاب میان فروشگاه‌های آنلاین و حضوری متناسب
          با سبک زندگی خود هستند.
        </p>
        <div class="s6-solution">
          <span class="s6-check">✓</span>
          <span>راهکار اوانو: شبکه ۹٬۴۱۵ پذیرنده فعال</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
