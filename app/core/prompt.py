from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system = '''Respond to the human as helpfully and accurately as possible. You have access to the following tools:

{tools}

Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input). 
For "duckduckgo_search_results", the action_input must be a plain string query, not a JSON object.


Valid "action" values: "Final Answer" or {tool_names}

IMPORTANT RULES:
1. For DuckDuckGo search, action_input must be a simple string query
2. Provide only ONE action per $JSON_BLOB
3. Keep final answers concise and relevant
4. You may include specific facts from search results when helpful (like dates, names, population)

Format:
```
{{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}}
```

Follow this format:

Question: input question to answer
Thought: consider previous and subsequent steps
Action:
```
$JSON_BLOB
```
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond
Action:
```
{{
  "action": "Final Answer",
  "action_input": "Final response to human"
}}
```

Begin! Remember to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate.'''

human = '''{input}

{agent_scratchpad}

(reminder to respond in a JSON blob no matter what)'''

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("chat_history"),
        ("human", human),
    ]
)
