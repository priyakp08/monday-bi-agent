import pandas as pd


def generate_metrics(deals_df, workorders_df):
    metrics = {}

    # Overall Counts
    metrics["total_deals"] = len(deals_df)
    metrics["total_workorders"] = len(workorders_df)

    # Deal Status
    if "Deal Status" in deals_df.columns:
        metrics["deal_status"] = (
            deals_df["Deal Status"]
            .value_counts(dropna=False)
            .to_dict()
        )

    # Deal Stage
    if "Deal Stage" in deals_df.columns:
        metrics["deal_stage"] = (
            deals_df["Deal Stage"]
            .value_counts(dropna=False)
            .to_dict()
        )

    # Sector Distribution
    if "Sector/service" in deals_df.columns:
        metrics["sector_distribution"] = (
            deals_df["Sector/service"]
            .value_counts(dropna=False)
            .to_dict()
        )

    # Deal Owners
    if "Owner code" in deals_df.columns:
        metrics["owner_distribution"] = (
            deals_df["Owner code"]
            .value_counts(dropna=False)
            .to_dict()
        )

    # Work Order Status
    if "Execution Status" in workorders_df.columns:
        metrics["execution_status"] = (
            workorders_df["Execution Status"]
            .value_counts(dropna=False)
            .to_dict()
        )

    # Billing Status
    if "Billing Status" in workorders_df.columns:
        metrics["billing_status"] = (
            workorders_df["Billing Status"]
            .value_counts(dropna=False)
            .to_dict()
        )

    # Missing Values
    metrics["missing_data"] = {
        "deals": deals_df.isna().sum().to_dict(),
        "workorders": workorders_df.isna().sum().to_dict()
    }

    return metrics
   