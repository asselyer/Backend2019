TASK_DONE = 1
TASK_TODO = 2
TASK_TESTED = 3
TASK_STATUSES = (
    (TASK_DONE, 'DONE'),
    (TASK_TODO, 'TODO'),
    (TASK_TESTED, 'TESTED'),
)

TASK_PRIORITY_LOW = 1
TASK_PRIORITY_MEDIUM = 2
TASK_PRIORITY_HIGH = 3
TASK_PRIORITIES = (
    (TASK_PRIORITY_LOW, 'low'),
    (TASK_PRIORITY_MEDIUM, 'medium'),
    (TASK_PRIORITY_HIGH, 'high'),
)

BLOCK_DONE = 1
BLOCK_TODO = 2
BLOCK_IN_PROGRESS = 3
BLOCK_CODE_REVIEW = 4
BLOCK_TYPES = (
    (BLOCK_DONE, 'DONE'),
    (BLOCK_TODO, 'TODO'),
    (BLOCK_IN_PROGRESS, 'IN PROGRESS'),
    (BLOCK_CODE_REVIEW, 'CODE REVIEW')
)