from memory.db import (
    save_milestone,
    save_decision,
    save_insight
)

# milestones
save_milestone(
    "Impact analysis engine implemented"
)

save_milestone(
    "Graph and association aggregation implemented"
)

save_milestone(
    "Historical insights integrated into impact analysis"
)

# decisions
save_decision(
    "Impact analysis built on top of graph merge engine"
)

save_decision(
    "Architecture intelligence combines static analysis with historical memory"
)

# insights
save_insight(
    "User model changes may affect multiple business flows",
    0.9
)

save_insight(
    "Associations significantly increase indirect refactor impact",
    0.95
)

save_insight(
    "Historical project memory improves legacy impact estimation",
    0.9
)

print("Impact analysis history saved")