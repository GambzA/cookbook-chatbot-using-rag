## AI Engineering Learning 1:
### Understand how LLMs actually behave, and get comfortable calling them directly — no frameworks yet.

 Understand transformers conceptually: tokens, context windows, embeddings, attention (why it matters practically, not the math derivation)
- [x] Learn core prompting patterns: zero-shot, few-shot, chain-of-thought, system vs. user prompts, structured output (JSON mode / schemas)
- [x] Make raw API calls (no LangChain, no SDK abstractions beyond the official client) — handle streaming responses, tool/function calling, multi-turn state yourself
- [x] Understand token economics: cost per model, context limits, prompt caching

**Resources:**
- [Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Anthropic Interactive Prompt Engineering Tutorial (GitHub)](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [Anthropic Cookbook (working code examples)](https://github.com/anthropics/anthropic-cookbook)
- [OpenAI Cookbook](https://cookbook.openai.com/)
- [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**About:**
Here I have create a simple code analyzer with Python and DeepSeek V4 Flash. 
The goal of this is to understand how tokens, context windows, and calling the API works.

The architectural flow is very simple:

- Get file contents of demo.html
- Pass it to DeepSeek as a text (I know, token heavy)
- And generate the out to analysis_output.md

**Observations:**

- DeepSeek is really cheap. With 85k tokens already I've only used up 0.01$
- Thinking set to 'disabled' does not work for some reason. 

