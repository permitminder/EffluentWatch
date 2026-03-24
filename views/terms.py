import streamlit as st


def show_terms_page():
    """Display the EffluentWatch Terms of Service page."""

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
    Terms of Service
</h1>
<p style="color: #6b6560; font-size: 14px; margin-bottom: 32px;">Last Updated: March 24, 2026</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">1. Acceptance of Terms</h3>
<p style="color: #3a3530; line-height: 1.7;">
By accessing or using EffluentWatch (effluentwatch.org), you agree to these Terms of Service. If you do not agree, do not use the platform.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">2. Description of Service</h3>
<p style="color: #3a3530; line-height: 1.7;">
EffluentWatch is an informational platform that reformats and displays publicly available discharge monitoring data from the EPA ECHO (Enforcement and Compliance History Online) system for Texas NPDES permits. EffluentWatch does not generate, verify, or independently confirm the accuracy of underlying government data.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">3. No Compliance Determinations</h3>
<p style="color: #3a3530; line-height: 1.7;">
EffluentWatch does not make legal or regulatory compliance determinations. The appearance of a facility or data record on this platform does not mean the facility is in violation of any law, regulation, or permit condition. Exceedance data reflects reported values compared to permit limits on file and may not account for variances, consent orders, compliance schedules, amended permits, reporting corrections, or other regulatory context.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">4. No Legal Advice</h3>
<p style="color: #3a3530; line-height: 1.7;">
Nothing on this platform constitutes legal, regulatory, environmental, financial, or investment advice. Consult qualified professionals before making decisions based on information obtained from EffluentWatch.
</p>
""", unsafe_allow_html=True)

    # Sections 5 and 6 — legal boilerplate in gray box
    st.markdown("""
<div style="background: #f5f3f0; border: 1px solid #e0ddd9; border-radius: 8px; padding: 24px 28px; margin: 24px 0;">

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">5. Disclaimer of Warranties</h3>
<p style="color: #3a3530; line-height: 1.7;">
THE SERVICE IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, COMPLETENESS, OR TIMELINESS OF DATA. EFFLUENTWATCH DOES NOT WARRANT THAT DATA IS CURRENT, CORRECT, OR COMPLETE.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">6. Limitation of Liability</h3>
<p style="color: #3a3530; line-height: 1.7;">
TO THE MAXIMUM EXTENT PERMITTED BY LAW, EFFLUENTWATCH AND ITS OPERATORS SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, OR ANY LOSS OF PROFITS OR REVENUES, WHETHER INCURRED DIRECTLY OR INDIRECTLY, OR ANY LOSS OF DATA, USE, GOODWILL, OR OTHER INTANGIBLE LOSSES, RESULTING FROM (A) YOUR ACCESS TO OR USE OF OR INABILITY TO ACCESS OR USE THE SERVICE; (B) ANY DATA OR INFORMATION OBTAINED FROM THE SERVICE; OR (C) ANY DECISIONS MADE BASED ON INFORMATION FROM THE SERVICE.
</p>
<p style="color: #3a3530; line-height: 1.7;">
IN NO EVENT SHALL EFFLUENTWATCH'S TOTAL LIABILITY EXCEED THE AMOUNT YOU PAID TO EFFLUENTWATCH IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">7. Indemnification</h3>
<p style="color: #3a3530; line-height: 1.7;">
You agree to indemnify and hold harmless EffluentWatch and its operators from any claims, damages, losses, or expenses (including reasonable attorney fees) arising from your use of the platform or your violation of these Terms.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">8. Data Accuracy and Timeliness</h3>
<p style="color: #3a3530; line-height: 1.7;">
EffluentWatch sources data from public government databases. Data is updated on a regular schedule but may not reflect the most recent submissions, corrections, or regulatory actions. Users should independently verify any information before relying on it for any purpose.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">9. Paid Services</h3>
<p style="color: #3a3530; line-height: 1.7;">
EffluentWatch Pro subscriptions are governed by these Terms. Subscriptions provide expanded access to data already sourced from public records. Refund policies are as described at the time of purchase. Paid access does not create any warranty of data accuracy, completeness, or timeliness beyond what is stated in these Terms.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">10. User Accounts and Email Alerts</h3>
<p style="color: #3a3530; line-height: 1.7;">
By providing your email address, you consent to receiving alert notifications related to your selected monitoring preferences. You may unsubscribe from alerts at any time using the unsubscribe link in any alert email. EffluentWatch will not sell or share your email address with third parties.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">11. Acceptable Use</h3>
<p style="color: #3a3530; line-height: 1.7;">
You may not use EffluentWatch to: (a) harass, defame, or threaten any person or entity; (b) misrepresent data obtained from the platform; (c) engage in securities trading based on non-public access to EffluentWatch data; or (d) scrape or bulk download data in a manner that degrades service performance.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">12. Modifications</h3>
<p style="color: #3a3530; line-height: 1.7;">
EffluentWatch may modify these Terms at any time. Continued use after changes constitutes acceptance.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">13. Governing Law</h3>
<p style="color: #3a3530; line-height: 1.7;">
These Terms are governed by the laws of the State of Texas without regard to conflict of law principles.
</p>

<h3 style="font-family: 'IBM Plex Mono', monospace; color: #1a1814;">14. Contact</h3>
<p style="color: #3a3530; line-height: 1.7;">
Questions about these Terms: <a href="mailto:legal@effluentwatch.org" style="color: #3a6b1a;">legal@effluentwatch.org</a>
</p>
""", unsafe_allow_html=True)
