import streamlit as st


def show_privacy_page():
    """Display the EffluentWatch Privacy Policy page."""

    if st.button("← Back"):
        st.session_state.current_view = "search"
        st.session_state.current_page = "search"
        st.rerun()

    st.markdown("""
<div class="pm-nav">
    <span class="pm-logo-mark">EW</span>
    <span class="pm-logo-text">EffluentWatch</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<h1 style="font-family: 'IBM Plex Mono', monospace; font-size: 28px; color: #1a1814; margin-bottom: 4px;">
    Privacy Policy
</h1>
<p style="color: #6b6560; font-size: 14px; margin-bottom: 32px;">Last Updated: March 24, 2026</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">1. Information We Collect</h3>
<p style="color: #3a3530; line-height: 1.7;">
<strong>Account Information:</strong> If you create an account or sign up for alerts, we collect your email address and alert preferences (facilities, parameters, or counties you choose to monitor).
</p>
<p style="color: #3a3530; line-height: 1.7;">
<strong>Payment Information:</strong> If you subscribe to EffluentWatch Pro, payment processing is handled by Stripe. We do not store your credit card number, bank account number, or other financial account information on our servers. Stripe's privacy policy governs the processing of your payment data.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">2. How We Use Your Information</h3>
<ul style="color: #3a3530; line-height: 1.7;">
    <li>To deliver email alerts based on your monitoring preferences</li>
    <li>To provide access to the platform and its features</li>
    <li>To respond to your inquiries or data correction requests</li>
    <li>To improve the platform</li>
</ul>
<p style="color: #3a3530; line-height: 1.7;">
We do not sell, rent, or share your personal information with third parties for marketing purposes.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">3. Data Retention</h3>
<p style="color: #3a3530; line-height: 1.7;">
We retain your email address and alert preferences for as long as your account is active or as needed to provide you with alerts. You may request deletion of your account and associated data at any time by contacting <a href="mailto:privacy@effluentwatch.org" style="color: #3a6b1a;">privacy@effluentwatch.org</a>.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">4. Data Security</h3>
<p style="color: #3a3530; line-height: 1.7;">
We implement reasonable security measures to protect your information. However, no method of electronic storage or transmission is 100% secure, and we cannot guarantee absolute security.
</p>
""", unsafe_allow_html=True)

    # Section 5 — Breach Notification in gray box
    st.markdown("""
<div style="background: #f5f3f0; border: 1px solid #e0ddd9; border-radius: 8px; padding: 24px 28px; margin: 24px 0;">

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">5. Breach Notification</h3>
<p style="color: #3a3530; line-height: 1.7;">
In the event of a data breach affecting your personal information, we will notify you in accordance with the Texas Identity Theft Enforcement and Protection Act (Tex. Bus. & Com. Code § 521.053) and any other applicable laws.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">6. Your Rights</h3>
<p style="color: #3a3530; line-height: 1.7;">You may at any time:</p>
<ul style="color: #3a3530; line-height: 1.7;">
    <li>Unsubscribe from email alerts using the link in any alert email</li>
    <li>Request a copy of the personal information we hold about you</li>
    <li>Request deletion of your account and associated data</li>
    <li>Contact us with questions about your data</li>
</ul>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">7. Children's Privacy</h3>
<p style="color: #3a3530; line-height: 1.7;">
EffluentWatch is not directed to children under 13. We do not knowingly collect personal information from children under 13.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">8. Changes to This Policy</h3>
<p style="color: #3a3530; line-height: 1.7;">
We may update this Privacy Policy from time to time. We will notify registered users of material changes via email.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">9. Contact</h3>
<p style="color: #3a3530; line-height: 1.7;">
Privacy inquiries: <a href="mailto:privacy@effluentwatch.org" style="color: #3a6b1a;">privacy@effluentwatch.org</a><br>
Data correction requests: <a href="mailto:data@effluentwatch.org" style="color: #3a6b1a;">data@effluentwatch.org</a>
</p>
""", unsafe_allow_html=True)
