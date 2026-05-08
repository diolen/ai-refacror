from memory.db import (
    save_milestone,
    save_decision,
    save_insight
)

# milestones
save_milestone(
    "Dependency graph v2 implemented"
)

save_milestone(
    "Model method mapping implemented"
)

save_milestone(
    "Component filtering added to dependency graph"
)

# decisions
save_decision(
    "Dependency graph limited to model interactions only"
)

save_decision(
    "CakePHP components excluded from architecture graph"
)

# insights
save_insight(
    "UsersController has high coupling with UsersOperationUnit model",
    0.9
)

save_insight(
    "User model is heavily used for CRUD operations",
    0.95
)

save_insight(
    "UsersOperationUnit contains domain-specific business logic",
    0.8
)

print("Graph v2 history saved")