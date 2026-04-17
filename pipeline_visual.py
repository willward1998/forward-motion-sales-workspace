#!/usr/bin/env python3
"""
Generate a visual infographic of the Forward Motion Medical sales pipeline.
Outputs: attachments/pipeline-overview.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import textwrap

# ── Palette ──────────────────────────────────────────────────────────────
BG          = "#0F1B2D"
CARD_BG     = "#182840"
ACCENT_LEAD = "#4DA8DA"   # blue
ACCENT_POT  = "#F5A623"   # amber
ACCENT_CUR  = "#27AE60"   # green
ACCENT_WARN = "#E74C3C"   # red  (at-risk / lost stages)
ACCENT_GRAY = "#7F8C8D"   # gray (nurture / inactive)
TEXT_WHITE   = "#F0F0F0"
TEXT_LIGHT   = "#B0BEC5"
TEXT_DIM     = "#6C7A89"
ARROW_COLOR  = "#4DA8DA"
GRAD_LINE   = "#2E4057"

# ── Pipeline data ────────────────────────────────────────────────────────
pipelines = [
    {
        "name": "LEADS",
        "subtitle": "New offices — not yet ordered",
        "color": ACCENT_LEAD,
        "graduation": "Billing received → Potential Provider",
        "stages": [
            {
                "name": "New Lead",
                "goal": "Identify as potential account",
                "action": "Send cold outreach or first call",
                "advance": "Will decides to reach out",
                "color": ACCENT_LEAD,
            },
            {
                "name": "Attempting Contact",
                "goal": "Make first contact",
                "action": "Follow up in 3–5 days, try different channel",
                "advance": "Outreach sent, awaiting response",
                "color": ACCENT_LEAD,
            },
            {
                "name": "Engaged",
                "goal": "Two-way conversation confirmed",
                "action": "Answer questions, offer demo/sample",
                "advance": "Doctor/OM responded with interest",
                "color": ACCENT_LEAD,
            },
            {
                "name": "Qualified",
                "goal": "Ready for billing & first order",
                "action": "Set up Doctor Portal, collect billing",
                "advance": "Decision-maker on board, billing in process",
                "color": ACCENT_LEAD,
            },
            {
                "name": "Nurture / Not Now",
                "goal": "Keep warm",
                "action": "30–60 day follow-up, light touch",
                "advance": "Interested but timing isn't right",
                "color": ACCENT_GRAY,
            },
            {
                "name": "Lost / Not a Fit",
                "goal": "Document and move on",
                "action": "Log reason, set 6-month reminder",
                "advance": "Office declined or not a fit",
                "color": ACCENT_WARN,
            },
        ],
    },
    {
        "name": "POTENTIAL PROVIDER",
        "subtitle": "Billing received — under $325 in orders",
        "color": ACCENT_POT,
        "graduation": "$325 in orders → Current Provider",
        "stages": [
            {
                "name": "Billing Received",
                "goal": "Get first order placed",
                "action": "Confirm portal, walk through first order",
                "advance": "First order submitted",
                "color": ACCENT_POT,
            },
            {
                "name": "Onboarding / 1st Order",
                "goal": "Great first experience",
                "action": "Check-in after delivery, encourage 2nd order",
                "advance": "First order delivered, office happy",
                "color": ACCENT_POT,
            },
            {
                "name": "Trialing",
                "goal": "Make ordering routine",
                "action": "Light touchpoints, mention scanning",
                "advance": "3 total devices ordered",
                "color": ACCENT_POT,
            },
            {
                "name": "Adopting",
                "goal": "Graduate — hit $325 threshold",
                "action": "Move to Current Provider pipeline",
                "advance": "$325 in orders (hard rule)",
                "color": ACCENT_POT,
            },
            {
                "name": "Stalled / At Risk",
                "goal": "Re-engage before losing account",
                "action": "Call first, then email. Find the blocker.",
                "advance": "No new orders for 30+ days",
                "color": ACCENT_WARN,
            },
        ],
    },
    {
        "name": "CURRENT PROVIDER",
        "subtitle": "Established accounts — 4+ devices ordered",
        "color": ACCENT_CUR,
        "graduation": None,
        "stages": [
            {
                "name": "New Provider",
                "goal": "Smooth transition from Potential",
                "action": "Welcome, confirm ongoing support",
                "advance": "Ordering consistently",
                "color": ACCENT_CUR,
            },
            {
                "name": "Active / Stable",
                "goal": "Healthy, consistent relationship",
                "action": "Regular check-ins, watch for gaps",
                "advance": "Maintained ordering pattern",
                "color": ACCENT_CUR,
            },
            {
                "name": "Growth Focused",
                "goal": "Grow order volume or referrals",
                "action": "Identify limits — scanning, more providers?",
                "advance": "High potential: multi-provider, high volume",
                "color": ACCENT_CUR,
            },
            {
                "name": "At Risk / Declining",
                "goal": "Prevent churn",
                "action": "Personal call first. Offer something concrete.",
                "advance": "Orders dropped noticeably",
                "color": ACCENT_WARN,
            },
            {
                "name": "Inactive / Churned",
                "goal": "Document, attempt win-back",
                "action": "One honest re-engagement attempt, then 90-day reminder",
                "advance": "No orders for 60+ days",
                "color": ACCENT_GRAY,
            },
        ],
    },
]


def draw_pipeline_infographic(output_path="attachments/pipeline-overview.png"):
    # ── Layout constants ─────────────────────────────────────────────
    fig_width = 30
    pipeline_col_width = 9.0
    col_gap = 1.2
    left_margin = 1.0

    # Stage card dimensions
    card_w = 8.0
    card_h = 2.0
    card_gap = 0.4

    # Calculate figure height
    max_stages = max(len(p["stages"]) for p in pipelines)
    header_h = 4.5
    stage_area_h = max_stages * (card_h + card_gap) + 1.5
    graduation_h = 2.0
    fig_height = header_h + stage_area_h + graduation_h + 1.0

    fig, ax = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, fig_width)
    ax.set_ylim(0, fig_height)
    ax.axis("off")

    # ── Title ────────────────────────────────────────────────────────
    ax.text(
        fig_width / 2, fig_height - 0.8,
        "FORWARD MOTION MEDICAL",
        ha="center", va="top",
        fontsize=28, fontweight="bold", color=TEXT_WHITE,
        fontfamily="sans-serif",
    )
    ax.text(
        fig_width / 2, fig_height - 1.6,
        "Sales Pipeline Overview",
        ha="center", va="top",
        fontsize=18, color=TEXT_LIGHT,
        fontfamily="sans-serif",
    )

    # Divider line under title
    ax.plot(
        [2, fig_width - 2], [fig_height - 2.1, fig_height - 2.1],
        color=GRAD_LINE, linewidth=1.5,
    )

    # ── Draw each pipeline column ────────────────────────────────────
    for pi, pipeline in enumerate(pipelines):
        col_x = left_margin + pi * (pipeline_col_width + col_gap)
        col_center = col_x + pipeline_col_width / 2

        # Pipeline header
        top_y = fig_height - 2.8

        # Header background pill
        header_pill = FancyBboxPatch(
            (col_x + 0.3, top_y - 1.05), card_w - 0.6, 1.3,
            boxstyle="round,pad=0.15",
            facecolor=pipeline["color"] + "20",
            edgecolor=pipeline["color"],
            linewidth=2,
        )
        ax.add_patch(header_pill)

        ax.text(
            col_center, top_y + 0.0,
            pipeline["name"],
            ha="center", va="center",
            fontsize=16, fontweight="bold",
            color=pipeline["color"],
            fontfamily="sans-serif",
        )
        ax.text(
            col_center, top_y - 0.55,
            pipeline["subtitle"],
            ha="center", va="center",
            fontsize=10, color=TEXT_LIGHT,
            fontfamily="sans-serif",
        )

        # ── Stage cards ──────────────────────────────────────────────
        stages_start_y = top_y - 1.8

        for si, stage in enumerate(pipeline["stages"]):
            card_x = col_x + (pipeline_col_width - card_w) / 2
            card_y = stages_start_y - si * (card_h + card_gap)

            # Card background
            card = FancyBboxPatch(
                (card_x, card_y - card_h), card_w, card_h,
                boxstyle="round,pad=0.18",
                facecolor=CARD_BG,
                edgecolor=stage["color"] + "80",
                linewidth=1.5,
            )
            ax.add_patch(card)

            # Stage number circle
            circle_r = 0.28
            circle_x = card_x + 0.55
            circle_y = card_y - 0.4
            circle = plt.Circle(
                (circle_x, circle_y), circle_r,
                facecolor=stage["color"],
                edgecolor="none",
            )
            ax.add_patch(circle)
            ax.text(
                circle_x, circle_y,
                str(si + 1),
                ha="center", va="center",
                fontsize=11, fontweight="bold", color=BG,
                fontfamily="sans-serif",
            )

            # Stage name
            ax.text(
                card_x + 1.1, circle_y,
                stage["name"],
                ha="left", va="center",
                fontsize=12, fontweight="bold", color=TEXT_WHITE,
                fontfamily="sans-serif",
            )

            # Goal
            ax.text(
                card_x + 0.4, card_y - 0.85,
                f"Goal: {stage['goal']}",
                ha="left", va="center",
                fontsize=9, color=TEXT_LIGHT,
                fontfamily="sans-serif",
            )

            # Action
            action_text = textwrap.fill(f"Action: {stage['action']}", width=55)
            ax.text(
                card_x + 0.4, card_y - 1.2,
                action_text,
                ha="left", va="center",
                fontsize=9, color=TEXT_DIM,
                fontfamily="sans-serif",
            )

            # Advance criteria (small, right-aligned)
            ax.text(
                card_x + card_w - 0.4, card_y - 1.65,
                f"▸ {stage['advance']}",
                ha="right", va="center",
                fontsize=8, color=stage["color"],
                fontfamily="sans-serif",
                style="italic",
            )

            # Arrow between stages (except last and except special stages)
            if si < len(pipeline["stages"]) - 1:
                # Don't draw arrow into "off-ramp" stages (last 1-2 stages that are gray/red)
                next_stage = pipeline["stages"][si + 1]
                arrow_y = card_y - card_h - card_gap / 2
                ax.annotate(
                    "", xy=(col_center, arrow_y + 0.12),
                    xytext=(col_center, arrow_y + card_gap - 0.12),
                    arrowprops=dict(
                        arrowstyle="->",
                        color=pipeline["color"] + "60",
                        lw=1.5,
                    ),
                )

        # ── Graduation arrow between pipelines ───────────────────────
        if pipeline["graduation"]:
            grad_y = stages_start_y - (len(pipeline["stages"])) * (card_h + card_gap) - 0.3
            next_col_x = left_margin + (pi + 1) * (pipeline_col_width + col_gap)
            next_col_center = next_col_x + pipeline_col_width / 2

            # Curved arrow from bottom of this column to top of next
            arrow_start_x = col_center + card_w / 2 + 0.2
            arrow_start_y = stages_start_y - 0.5 * (card_h + card_gap)  # mid pipeline
            arrow_end_x = next_col_x + (pipeline_col_width - card_w) / 2 - 0.1
            arrow_end_y = stages_start_y - 0.5 * (card_h + card_gap)

            # Simple horizontal graduation arrow between columns
            mid_y = stages_start_y - 1.0
            ax.annotate(
                "",
                xy=(col_x + pipeline_col_width + 0.05, mid_y),
                xytext=(col_x + pipeline_col_width + col_gap - 0.05, mid_y),
                arrowprops=dict(
                    arrowstyle="<-",
                    color=pipeline["color"],
                    lw=2.5,
                    connectionstyle="arc3,rad=0",
                ),
            )
            # Graduation label
            grad_label = pipeline["graduation"].split("→")[0].strip()
            ax.text(
                col_x + pipeline_col_width + col_gap / 2,
                mid_y + 0.25,
                grad_label,
                ha="center", va="bottom",
                fontsize=8, color=pipeline["color"],
                fontfamily="sans-serif", fontweight="bold",
                rotation=0,
            )

    # ── Footer ───────────────────────────────────────────────────────
    ax.text(
        fig_width / 2, 0.4,
        "Forward Motion Medical  •  Custom Orthotics Lab  •  Pipeline Reference",
        ha="center", va="center",
        fontsize=10, color=TEXT_DIM,
        fontfamily="sans-serif",
    )

    plt.tight_layout(pad=0.5)
    plt.savefig(output_path, dpi=150, facecolor=BG, bbox_inches="tight")
    plt.close()
    print(f"✓ Saved to {output_path}")


if __name__ == "__main__":
    draw_pipeline_infographic()
