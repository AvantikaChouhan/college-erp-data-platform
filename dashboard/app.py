"""
Campus ERP — Insights Dashboard
A Streamlit rebuild of the college ERP analytics dashboard.

Run with:
    streamlit run app.py

Expects a `data/` folder alongside this file containing the 10 CSV exports.
"""

import os
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# -----------------------------------------------------------------------
# Page config
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="Campus ERP — Insights Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------
# Theme tokens (Navy & Gold)
# -----------------------------------------------------------------------
NAVY_950 = "#040F26"
NAVY_900 = "#0A1F44"
NAVY_800 = "#12335E"
NAVY_700 = "#1D4B85"
NAVY_L = "#7C93B8"
GOLD_500 = "#C9A227"
GOLD_400 = "#E0BE4E"
GOLD_100 = "#F6ECC6"
RED = "#B23A2E"
AMBER = "#C1791E"
GREEN = "#2F7A4F"
INFO = "#2A6F97"
SLATE = "#8C9BB5"
CREAM = "#F6F4EC"
BORDER = "#E4DFCF"
TEXT = "#152238"
TEXT_SECONDARY = "#5B6B85"

RISK_COLORS = {
    "Critical Risk": RED,
    "Moderate Risk": AMBER,
    "Academic Risk Only": NAVY_L,
    "Fee Pending Only": INFO,
    "Low Risk": GREEN,
}
PAY_COLORS = {"Paid": GREEN, "Partial": AMBER, "Pending": RED}
PLOTLY_FONT = dict(family="Inter, -apple-system, Segoe UI, sans-serif", color=TEXT_SECONDARY)

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"]  {{
    font-family: 'Inter', sans-serif;
}}
.stApp {{
    background-color: {CREAM};
    color: {TEXT};
}}
/* Force readable text in the MAIN content area only — scoped tightly so
   it can never override the sidebar's own cream/gold colors below. */
[data-testid="stAppViewContainer"] > .main p,
[data-testid="stAppViewContainer"] > .main span,
[data-testid="stAppViewContainer"] > .main label,
[data-testid="stAppViewContainer"] > .main [data-testid="stMarkdownContainer"] p,
[data-testid="stAppViewContainer"] > .main [data-testid="stMetricLabel"],
[data-testid="stAppViewContainer"] > .main [data-testid="stMetricValue"],
[data-testid="stAppViewContainer"] > .main [data-testid="stWidgetLabel"] p {{
    color: {TEXT} !important;
}}
[data-testid="stAppViewContainer"] > .main [data-testid="stCaptionContainer"],
[data-testid="stAppViewContainer"] > .main [data-testid="stCaptionContainer"] p {{
    color: {TEXT_SECONDARY} !important;
}}
.panel-note {{ color: {TEXT_SECONDARY} !important; }}
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {NAVY_950}, {NAVY_900} 60%);
}}
[data-testid="stSidebar"] * {{
    color: #EDE7D3 !important;
}}
[data-testid="stSidebar"] .stRadio label {{
    font-size: 14.5px;
}}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {{
    color: #9FB0C9 !important;
}}
h1, h2, h3 {{
    font-family: 'Fraunces', Georgia, serif !important;
    color: {TEXT};
}}
.kpi-card {{
    background:#FFFFFF; border:1px solid {BORDER}; border-left:4px solid {GOLD_500};
    border-radius:6px; padding:14px 16px; margin-bottom:8px;
}}
.kpi-card.alt{{ border-left-color:{NAVY_800}; }}
.kpi-card.risk{{ border-left-color:{RED}; }}
.kpi-num {{
    font-family:'Fraunces', Georgia, serif; font-size:26px; font-weight:600; color:{TEXT}; line-height:1.1;
}}
.kpi-label {{
    font-size:12px; color:{TEXT_SECONDARY}; margin-top:4px; line-height:1.4;
}}
.panel-note {{ font-size:12.5px; color:{TEXT_SECONDARY}; margin-bottom:6px; }}
.brand-word {{
    font-family:'Fraunces', Georgia, serif; font-size:20px; font-weight:600; color:#F7EFD6;
}}
.brand-sub {{ font-size:12px; color:#9FB0C9; line-height:1.5; }}
hr {{ border-color: {BORDER}; }}
.tag {{ display:inline-block; padding:2px 9px; border-radius:20px; font-size:11px; font-weight:600; }}
.tag.paid, .tag.placed {{ background:#E4F3E9; color:{GREEN}; }}
.tag.partial {{ background:#FBF0DA; color:{AMBER}; }}
.tag.pending {{ background:#FAE4E1; color:{RED}; }}
.tag.notplaced {{ background:#E7EBF3; color:{TEXT_SECONDARY}; }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------
# Data loading
# -----------------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


@st.cache_data
def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(DATA_DIR, name))


@st.cache_data
def load_all():
    return {
        "insight_df": load_csv("insight_df.csv"),
        "top_packages": load_csv("top_packages.csv"),
        "company_insights": load_csv("company_insights.csv"),
        "semester_insights": load_csv("semester_insights.csv"),
        "fee_academic_insights": load_csv("fee_academic_insights.csv"),
        "placement_insights": load_csv("placement_insights.csv"),
        "attendance_performance": load_csv("attendance_performance.csv"),
        "student_segments": load_csv("student_segments.csv"),
        "department_360": load_csv("department_360.csv"),
        "students": load_csv("student_analytics.csv"),
    }


try:
    DATA = load_all()
except FileNotFoundError as e:
    st.error(
        "Couldn't find the data files. Make sure the `data/` folder "
        "(with all 10 CSVs) sits next to app.py.\n\n"
        f"Details: {e}"
    )
    st.stop()

DEPARTMENTS = sorted(DATA["students"]["department"].unique().tolist())


# -----------------------------------------------------------------------
# Small helpers
# -----------------------------------------------------------------------
def fmt_money(n: float) -> str:
    n = float(n)
    if n >= 1e7:
        return f"₹{n/1e7:.2f} Cr"
    if n >= 1e5:
        return f"₹{n/1e5:.2f} L"
    return f"₹{n:,.0f}"


def kpi_card(label, value, variant=""):
    cls = f"kpi-card {variant}".strip()
    st.markdown(
        f'<div class="{cls}"><div class="kpi-num">{value}</div>'
        f'<div class="kpi-label">{label}</div></div>',
        unsafe_allow_html=True,
    )


def kpi_row(items):
    cols = st.columns(len(items))
    for c, (label, value, variant) in zip(cols, items):
        with c:
            kpi_card(label, value, variant)


def style_fig(fig, height=320, has_xaxis_title=False):
    # Extra bottom margin/offset when there's both a horizontal legend and an
    # x-axis title, so the two don't render on top of each other.
    bottom_margin = 70 if has_xaxis_title else 45
    legend_y = -0.42 if has_xaxis_title else -0.22
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=30, b=bottom_margin),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=PLOTLY_FONT,
        legend=dict(orientation="h", yanchor="top", y=legend_y, x=0.5, xanchor="center"),
    )
    fig.update_xaxes(gridcolor="rgba(10,31,68,0.07)")
    fig.update_yaxes(gridcolor="rgba(10,31,68,0.07)")
    return fig


def dept_pill_filter(page_key: str) -> str:
    """A horizontal department slicer, styled like pills via st.radio(horizontal=True)."""
    return st.radio(
        "Department",
        options=["All"] + DEPARTMENTS,
        horizontal=True,
        key=f"dept_{page_key}",
    )


def scope_students(dept: str) -> pd.DataFrame:
    df = DATA["students"]
    return df if dept == "All" else df[df["department"] == dept]


# -----------------------------------------------------------------------
# Sidebar navigation
# -----------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div class="brand-word">🎓 Campus ERP</div>'
        '<div class="brand-sub">Institutional insights across academics, '
        "fees and placements — 500 students, 5 departments.</div><hr>",
        unsafe_allow_html=True,
    )
    page = st.radio(
        "Navigate",
        [
            "Overview",
            "Academics & Attendance",
            "Fees & Risk",
            "Placements",
            "Departments & Students",
        ],
        label_visibility="collapsed",
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.caption("Data source: end-of-term ERP export")
    st.caption(f"{len(DEPARTMENTS)} departments · 8 semesters · {len(DATA['students'])} student records")


# =========================================================================
# PAGE 1 — OVERVIEW
# =========================================================================
if page == "Overview":
    st.title("Overview")
    st.caption("A snapshot of the student body across academics, attendance, fees and placement outcomes.")

    ins = DATA["insight_df"].iloc[0]
    kpi_row(
        [
            ("Total students", f"{int(ins['total_students']):,}", "alt"),
            ("Academic risk students", f"{int(ins['academic_risk_students']):,}", "risk"),
            ("Attendance risk students", f"{int(ins['attendance_risk_students']):,}", "risk"),
            ("Fee + academic risk", f"{int(ins['fee_academic_risk_students']):,}", "risk"),
        ]
    )
    kpi_row(
        [
            ("High performers, unplaced", f"{int(ins['high_performers_unplaced']):,}", ""),
            ("Academically strong", f"{int(ins['academically_strong_students']):,}", ""),
            ("Students with pending fees", f"{int(ins['students_with_pending_fees']):,}", "alt"),
        ]
    )

    st.write("")
    c1, c2 = st.columns([1.3, 1])
    with c1:
        st.subheader("Department snapshot")
        st.markdown('<div class="panel-note">Average marks vs. average attendance</div>', unsafe_allow_html=True)
        dept = DATA["department_360"]
        fig = go.Figure()
        fig.add_bar(name="Avg marks", x=dept["department"], y=dept["avg_marks"], marker_color=NAVY_900)
        fig.add_bar(name="Avg attendance %", x=dept["department"], y=dept["avg_attendance"], marker_color=GOLD_500)
        fig.update_layout(barmode="group")
        st.plotly_chart(style_fig(fig), use_container_width=True)

    with c2:
        st.subheader("Student segments")
        st.markdown('<div class="panel-note">500 students</div>', unsafe_allow_html=True)
        seg = DATA["student_segments"]
        fig = go.Figure(
            go.Pie(
                labels=seg["student_segment"],
                values=seg["students"],
                hole=0.62,
                marker_colors=[NAVY_900, RED, GOLD_500, AMBER, GREEN],
            )
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)

    st.subheader("Institution-wide risk segmentation")
    st.markdown(
        '<div class="panel-note">Students grouped by combined academic &amp; fee risk</div>',
        unsafe_allow_html=True,
    )
    order = ["Critical Risk", "Moderate Risk", "Academic Risk Only", "Fee Pending Only", "Low Risk"]
    risk = DATA["fee_academic_insights"].set_index("risk_category").loc[order].reset_index()
    fig = go.Figure(
        go.Bar(
            x=risk["students"],
            y=risk["risk_category"],
            orientation="h",
            marker_color=[RISK_COLORS.get(r, SLATE) for r in risk["risk_category"]],
        )
    )
    st.plotly_chart(style_fig(fig, height=260), use_container_width=True)


# =========================================================================
# PAGE 2 — ACADEMICS & ATTENDANCE
# =========================================================================
elif page == "Academics & Attendance":
    st.title("Academics & Attendance")
    st.caption("Marks and attendance trends across semesters, filterable by department.")

    dept = dept_pill_filter("academics")
    scope = scope_students(dept)

    strong = int((scope["avg_marks"] >= 75).sum())
    att_risk = int((scope["avg_attendance"] < 75).sum())
    kpi_row(
        [
            ("Students in scope", f"{len(scope):,}", "alt"),
            ("Average marks", f"{scope['avg_marks'].mean():.1f}", ""),
            ("Average attendance %", f"{scope['avg_attendance'].mean():.1f}", ""),
        ]
    )
    kpi_row(
        [
            ("Below 75% attendance", f"{att_risk:,}", "risk"),
            ("Marks ≥ 75 (strong)", f"{strong:,}", ""),
        ]
    )

    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Average marks & attendance by semester")
        by_sem = (
            scope.groupby("semester")[["avg_marks", "avg_attendance"]]
            .mean()
            .reindex(range(1, 9))
            .reset_index()
        )
        fig = go.Figure()
        fig.add_scatter(
            x=by_sem["semester"], y=by_sem["avg_marks"], name="Avg marks",
            line=dict(color=NAVY_900, width=3), fill="tozeroy", fillcolor="rgba(10,31,68,0.08)",
        )
        fig.add_scatter(
            x=by_sem["semester"], y=by_sem["avg_attendance"], name="Avg attendance %",
            line=dict(color=GOLD_500, width=3), fill="tozeroy", fillcolor="rgba(201,162,39,0.12)",
        )
        fig.update_xaxes(title=dict(text="Semester", standoff=15), dtick=1)
        st.plotly_chart(style_fig(fig, has_xaxis_title=True), use_container_width=True)

    with c2:
        st.subheader("Attendance distribution")
        bins = [0, 60, 75, 85, 101]
        labels = ["Below 60%", "60% – 74%", "75% – 84%", "85%+"]
        band = pd.cut(scope["avg_attendance"], bins=bins, labels=labels, right=False)
        counts = band.value_counts().reindex(labels).fillna(0)
        fig = go.Figure(
            go.Bar(x=labels, y=counts.values, marker_color=[RED, AMBER, INFO, GREEN])
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)

    st.subheader("Attendance vs. academic performance")
    st.markdown(
        '<div class="panel-note">Institution-wide reference — average marks by attendance band</div>',
        unsafe_allow_html=True,
    )
    corr = DATA["attendance_performance"]
    fig = go.Figure(go.Bar(x=corr["attendance_band"], y=corr["average_marks"], marker_color=NAVY_700))
    st.plotly_chart(style_fig(fig, height=240), use_container_width=True)
    st.caption(
        "Students attending 75% or more of classes average noticeably higher marks "
        "than those below 60% attendance."
    )


# =========================================================================
# PAGE 3 — FEES & RISK
# =========================================================================
elif page == "Fees & Risk":
    st.title("Fees & Risk")
    st.caption("Fee collection status and combined academic + financial risk segmentation.")

    dept = dept_pill_filter("fees")
    scope = scope_students(dept)

    total_pending = scope["pending_amount"].sum()
    pending_students = int((scope["pending_amount"] > 0).sum())
    collection_rate = (
        scope["amount_paid"].sum() / scope["total_fee"].sum() * 100 if scope["total_fee"].sum() else 0
    )
    kpi_row(
        [
            ("Students in scope", f"{len(scope):,}", "alt"),
            ("Total pending fees", fmt_money(total_pending), "risk"),
            ("Students with pending fees", f"{pending_students:,}", "risk"),
            ("Fee collection rate", f"{collection_rate:.1f}%", ""),
        ]
    )

    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Payment status")
        st.markdown('<div class="panel-note">Filtered by department slicer</div>', unsafe_allow_html=True)
        counts = scope["payment_status"].value_counts().reindex(["Paid", "Partial", "Pending"]).fillna(0)
        fig = go.Figure(
            go.Pie(
                labels=counts.index, values=counts.values, hole=0.62,
                marker_colors=[PAY_COLORS[s] for s in counts.index],
            )
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)

    with c2:
        st.subheader("Pending fees by department")
        d360 = DATA["department_360"]
        colors = [GOLD_500 if d == dept else NAVY_900 for d in d360["department"]]
        fig = go.Figure(go.Bar(x=d360["department"], y=d360["pending_fees"], marker_color=colors))
        fig.update_yaxes(tickprefix="₹")
        st.plotly_chart(style_fig(fig), use_container_width=True)

    st.subheader("Risk category breakdown")
    st.markdown(
        '<div class="panel-note">Institution-wide — combined academic &amp; fee risk</div>',
        unsafe_allow_html=True,
    )
    risk_tbl = DATA["fee_academic_insights"].copy()
    risk_tbl["total_pending_fees"] = risk_tbl["total_pending_fees"].apply(fmt_money)
    st.dataframe(risk_tbl, use_container_width=True, hide_index=True)


# =========================================================================
# PAGE 4 — PLACEMENTS
# =========================================================================
elif page == "Placements":
    st.title("Placements")
    st.caption("Placement outcomes, recruiting companies and top packages by department.")

    dept = dept_pill_filter("placements")
    scope = scope_students(dept)
    placed = scope[scope["placement_status"] == "Placed"]
    not_placed = scope[scope["placement_status"] != "Placed"]

    placement_rate = len(placed) / len(scope) * 100 if len(scope) else 0
    kpi_row(
        [
            ("Students in scope", f"{len(scope):,}", "alt"),
            ("Placed students", f"{len(placed):,}", ""),
            ("Placement rate", f"{placement_rate:.1f}%", ""),
        ]
    )
    kpi_row(
        [
            ("Average package (LPA)", f"{placed['package_lpa'].mean():.2f}" if len(placed) else "0.00", ""),
            ("Highest package (LPA)", f"{placed['package_lpa'].max():.2f}" if len(placed) else "0.00", "alt"),
        ]
    )

    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Placement rate by department")
        pi = DATA["placement_insights"]
        colors = [GOLD_500 if d == dept else NAVY_900 for d in pi["department"]]
        fig = go.Figure(go.Bar(x=pi["department"], y=pi["placement_rate"], marker_color=colors))
        st.plotly_chart(style_fig(fig), use_container_width=True)

    with c2:
        st.subheader("Placed vs. not placed")
        st.markdown('<div class="panel-note">Average marks &amp; attendance, selected scope</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_bar(
            name="Placed",
            x=["Avg marks", "Avg attendance %"],
            y=[placed["avg_marks"].mean() if len(placed) else 0, placed["avg_attendance"].mean() if len(placed) else 0],
            marker_color=GOLD_500,
        )
        fig.add_bar(
            name="Not placed",
            x=["Avg marks", "Avg attendance %"],
            y=[not_placed["avg_marks"].mean() if len(not_placed) else 0, not_placed["avg_attendance"].mean() if len(not_placed) else 0],
            marker_color=NAVY_900,
        )
        fig.update_layout(barmode="group")
        st.plotly_chart(style_fig(fig), use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.subheader("Top recruiting companies")
        st.markdown('<div class="panel-note">By students placed</div>', unsafe_allow_html=True)
        comp = DATA["company_insights"].sort_values("placed_students", ascending=True)
        fig = go.Figure(go.Bar(x=comp["placed_students"], y=comp["company"], orientation="h", marker_color=NAVY_700))
        st.plotly_chart(style_fig(fig), use_container_width=True)

    with c4:
        st.subheader("Highest packages offered")
        st.markdown('<div class="panel-note">Top 10 offers, LPA</div>', unsafe_allow_html=True)
        top = DATA["top_packages"].sort_values("package_lpa", ascending=False).head(10)
        st.dataframe(
            top[["student_name", "department", "company", "package_lpa"]],
            use_container_width=True, hide_index=True,
        )


# =========================================================================
# PAGE 5 — DEPARTMENTS & STUDENTS
# =========================================================================
elif page == "Departments & Students":
    st.title("Departments & Students")
    st.caption("Full department comparison and a searchable record-level student explorer.")

    st.subheader("Department 360")
    st.markdown('<div class="panel-note">Click a column heading to sort</div>', unsafe_allow_html=True)
    st.dataframe(DATA["department_360"], use_container_width=True, hide_index=True)

    st.write("")
    st.subheader("Student explorer")
    st.markdown('<div class="panel-note">Search and filter all 500 records</div>', unsafe_allow_html=True)

    f1, f2, f3, f4 = st.columns([2, 1, 1, 1])
    with f1:
        query = st.text_input("Search name or roll no", "")
    with f2:
        dept_f = st.selectbox("Department", ["All"] + DEPARTMENTS)
    with f3:
        placement_f = st.selectbox("Placement", ["All", "Placed", "Not Placed"])
    with f4:
        payment_f = st.selectbox("Payment", ["All", "Paid", "Partial", "Pending"])

    df = DATA["students"].copy()
    if dept_f != "All":
        df = df[df["department"] == dept_f]
    if placement_f != "All":
        df = df[df["placement_status"] == placement_f]
    if payment_f != "All":
        df = df[df["payment_status"] == payment_f]
    if query:
        q = query.lower()
        df = df[
            df["student_name"].str.lower().str.contains(q)
            | df["roll_no"].str.lower().str.contains(q)
        ]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Students matched", f"{len(df):,}")
    m2.metric("Avg marks", f"{df['avg_marks'].mean():.1f}" if len(df) else "—")
    m3.metric("Avg attendance", f"{df['avg_attendance'].mean():.1f}%" if len(df) else "—")
    m4.metric("Pending fees", fmt_money(df["pending_amount"].sum()) if len(df) else "—")

    show_cols = [
        "roll_no", "student_name", "department", "semester", "avg_attendance",
        "avg_marks", "payment_status", "placement_status", "company", "package_lpa",
    ]
    st.dataframe(df[show_cols].head(200), use_container_width=True, hide_index=True)
    if len(df) > 200:
        st.caption(f"Showing first 200 of {len(df):,} matching records — refine filters to narrow further.")
    else:
        st.caption(f"Showing all {len(df):,} matching records.")
