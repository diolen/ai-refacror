from memory.db import (
    save_milestone,
    save_decision,
    save_insight
)

# milestones
save_milestone(
    "Initial ai-refactor project structure created"
)

save_milestone(
    "SQLite memory system initialized"
)

save_milestone(
    "CLI refactor workflow successfully executed"
)

save_milestone(
    "Dependency scanner v1 implemented"
)

save_milestone(
    "Automatic pattern extraction implemented"
)

# decisions
save_decision(
    "AI tooling separated from CakePHP legacy project"
)

save_decision(
    "SQLite chosen instead of vector database"
)

save_decision(
    "No agent-based architecture allowed"
)

save_decision(
    "Ollama local models used as transformation layer"
)

# insights
save_insight(
    "CakePHP 2 controllers show high model coupling",
    0.9
)

save_insight(
    "Large context windows cause instability on CPU-only hardware",
    0.95
)

print("Bootstrap history saved")