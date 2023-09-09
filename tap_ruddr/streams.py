"""Stream type classes for tap-ruddr."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_ruddr.client import ruddrStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class ClientsStream(ruddrStream):
    """Define custom stream."""

    name = "clients"
    path = "/clients"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "clients.json"  # noqa: ERA001

class ProjectsStream(ruddrStream):
    name = "projects"
    path = "/projects"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "projects.json"


class ProjectMembersStream(ruddrStream):
    name = "project-members"
    path = "/project-members"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-members.json"

class ProjectRolesStream(ruddrStream):
    name = "project-roles"
    path = "/project-roles"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-roles.json"

class ProjectTasksStream(ruddrStream):
    name = "project-tasks"
    path = "/project-tasks"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-tasks.json"

class ProjectExpensesStream(ruddrStream):
    name = "project-expenses"
    path = "/project-expenses"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-expenses.json"

class ProjectOtherItemsStream(ruddrStream):
    name = "project-other-items"
    path = "/project-other-items"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-other-items.json"

class TimeEntriesStream(ruddrStream):
    name = "time-entries"
    path = "/time-entries"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "time-entries.json"

class AllocationsStream(ruddrStream):
    name = "allocations"
    path = "/allocations"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "allocations.json"

class MembersStream(ruddrStream):
    name = "members"
    path = "/members"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "members.json"
    
class ProjectRevenueRecognitionEntriesStream(ruddrStream):
    name = "project-revenue-recognition-entries"
    path = "/project-revenue-recognition-entries"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-revenue-recognition-entries.json"
    
class ProjectBudgetExpensesStream(ruddrStream):
    name = "project-budget-expenses"
    path = "/project-budget-expenses"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-budget-expenses.json"
    
class ProjectBudgetOtherItemsStream(ruddrStream):
    name = "project-budget-other-items"
    path = "/project-budget-other-items"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-budget-other-items.json"
    
class ProjectInvoiceMilestonesStream(ruddrStream):
    name = "project-invoice-milestones"
    path = "/project-invoice-milestones"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-invoice-milestones.json"
    
class ProjectMonthlyBudgetExpensesStream(ruddrStream):
    name = "project-monthly-budget-expenses"
    path = "/project-monthly-budget-expenses"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-monthly-budget-expenses.json"
    
class ProjectMonthlyBudgetOtherItemsStream(ruddrStream):
    name = "project-monthly-budget-other-items"
    path = "/project-monthly-budget-other-items"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "project-monthly-budget-other-items.json"
    
class ExpenseItemsStream(ruddrStream):
    name = "expense-items"
    path = "/expense-items"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "expense-items.json"
    
class ExpenseReportsStream(ruddrStream):
    name = "expense-reports"
    path = "/expense-reports"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = '$.results[*]'
    schema_filepath = SCHEMAS_DIR / "expense-reports.json"