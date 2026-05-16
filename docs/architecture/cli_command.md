## Tests
python tests/smoke/test_prompt_compiler.py
python -m tests.smoke.test_prompt_compiler
python tests/smoke/validate_system.py

python cli.py prompt User ../app/Controller/SicsController.php ../app/Model/Sics.php --mode impact


## Генерация тестового промпта для фичи
python -c "from analysis.core.prompt_builder.compiler import PromptCompiler; from analysis.core.prompt_builder.enums import TaskType; from analysis.core.prompt_builder.prompt_context import PromptContext;
entity_model={'User':{'methods':['find','save','delete','customBusinessLogic'],'dependencies':['DB','Cache'],'associations':{'hasMany':['Order'],'belongsTo':['Group']}}}
compiler=PromptCompiler(entity_model, PromptContext())
print(compiler.compile(TaskType.FEATURE,'User'))"

## Генерация тестового промпта для рефакторинга
python -c "from analysis.core.prompt_builder.compiler import PromptCompiler; from analysis.core.prompt_builder.enums import TaskType; from analysis.core.prompt_builder.prompt_context import PromptContext;
entity_model={'User':{'methods':['find','save','delete','customBusinessLogic'],'dependencies':['DB','Cache'],'associations':{'hasMany':['Order'],'belongsTo':['Group']}}}
compiler=PromptCompiler(entity_model, PromptContext())
print(compiler.compile(TaskType.REFACTOR,'User'))"

## Генерация тестового промпта для дебага
python -c "from analysis.core.prompt_builder.compiler import PromptCompiler; from analysis.core.prompt_builder.enums import TaskType; from analysis.core.prompt_builder.prompt_context import PromptContext;
entity_model={'User':{'methods':['find','save','delete','customBusinessLogic'],'dependencies':['DB','Cache'],'associations':{'hasMany':['Order'],'belongsTo':['Group']}}}
compiler=PromptCompiler(entity_model, PromptContext())
print(compiler.compile(TaskType.DEBUG,'User'))"


