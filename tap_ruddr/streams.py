"""Stream type classes for tap-ruddr."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_ruddr.client import ruddrStream

# TODO: Delete this is if not using json files for schema definition
#SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class ClientsStream(ruddrStream):
    """Define custom stream."""

    name = "clients"
    path = "/clients"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.[*]'
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("key", th.StringType),
        th.Property("name", th.StringType),
        th.Property("code", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("notes", th.StringType),
        th.Property("emails", th.ArrayType(th.StringType)),
        th.Property("streetAddress", th.StringType),
        th.Property("useWorkspaceInvoiceDetails", th.BooleanType),
        th.Property("paymentTermsId", th.StringType),
        th.Property("invoiceNotes", th.StringType),
        th.Property("isInternal", th.BooleanType),
        th.Property("recordStatusId", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("practice", th.StringType),
        th.Property(
            "owner",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType)
            )
        ),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType)
                )
            )
        )
    ).to_dict() 

class ProjectsStream(ruddrStream):
    name = "projects"
    path = "/projects"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("key", th.StringType),
        th.Property("name", th.StringType),
        th.Property("notes", th.StringType),
        th.Property("statusId", th.StringType),
        th.Property("start", th.DateType),
        th.Property("end", th.DateType),
        th.Property("code", th.StringType),
        th.Property("poNumber", th.StringType),
        th.Property("billingTypeId", th.StringType),
        th.Property("isBillable", th.BooleanType),
        th.Property("currency", th.StringType),
        th.Property("revenueRecognitionMethod", th.StringType),
        th.Property("fixedFee", th.NumberType),
        th.Property("fixedRecurringFee", th.NumberType),
        th.Property("fixedRecurringStart", th.StringType),
        th.Property("fixedRecurringEnd", th.StringType),
        th.Property("useRoles", th.BooleanType),
        th.Property("useBudget", th.BooleanType),
        th.Property("budgetMode", th.StringType),
        th.Property("useMonthlyBudget", th.BooleanType),
        th.Property("monthlyBudgetMode", th.StringType),
        th.Property("recordStatusId", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property(
            "client",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType)
            )
        ),
        th.Property(
            "practice",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType)
            )
        ),
        th.Property(
            "projectType",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType)
            )
        ),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType)
                )
            )
        ),
        th.Property(
            "budget",
            th.ObjectType(
                th.Property("revenue", th.NumberType),
                th.Property("servicesRevenue", th.NumberType),
                th.Property("otherRevenue", th.NumberType),
                th.Property("billableExpenses", th.NumberType),
                th.Property("nonBillableExpenses", th.NumberType),
                th.Property("billableHours", th.NumberType),
                th.Property("nonBillableHours", th.NumberType)
            )
        ),
        th.Property(
            "monthlyBudget",
            th.ObjectType(
                th.Property("revenue", th.NumberType),
                th.Property("servicesRevenue", th.NumberType),
                th.Property("otherRevenue", th.NumberType),
                th.Property("billableExpenses", th.NumberType),
                th.Property("nonBillableExpenses", th.NumberType),
                th.Property("billableHours", th.NumberType),
                th.Property("nonBillableHours", th.NumberType)
            )
        )
    ).to_dict()

class ProjectMembersStream(ruddrStream):
    name = "project-members"
    path = "/project-members"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("typeId", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("isBillable",th.BooleanType),
        th.Property("rate", th.NumberType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("project", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("client", th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType)
            ))
        )),
        th.Property("member", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType)
        )),
        th.Property("roles", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType)
            )
        )),
        th.Property("budget", th.NumberType),
        th.Property("monthlyBudget", th.NumberType)
    ).to_dict()