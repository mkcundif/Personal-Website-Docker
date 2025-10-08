# AI Dev Notes

## Prompts used

1) Prompt: "Create a responsive multi-page personal website scaffold with HTML and CSS, include pages index, about, resume, projects, contact, and a contact form that validates password match client-side."

AI output: Generated initial HTML and CSS files with navigation and a minimal contact form.

Response: Accepted and modified — I updated text content, added accessibility attributes, and adjusted the CSS color scheme.


2) Prompt: "Add a .prompt/dev_notes.md file template that logs prompts, AI outputs, and a short reflection."

AI output: Created a basic markdown structure for logging prompts and reflections.

Response: Accepted.


3) Prompt: "Create a contact form with HTML5 validation for required fields and JavaScript to ensure password and confirm password match; redirect to thank you page on success."

AI output: Form with required attributes and a submit handler that checks password equality.

Response: Accepted with modifications — changed form method to GET for static demo and added clear alert messages.


## 150-word reflection

AI tools accelerated scaffolding by generating boilerplate HTML and CSS quickly. Using AI saved time on repetitive layout and navigation structure so I could focus on content, accessibility, and styling choices. AI sometimes produced code that assumed runtime backends (e.g., server-side form handling) which I adapted to a static site flow. I also corrected minor accessibility omissions (labels and alt text) the AI initially missed. I treated each AI suggestion critically, accepting useful code, modifying styling and semantics, and rejecting anything that didn't follow best practices. This workflow helped me move faster while retaining educational value. In future, I'll keep AI for scaffolding and testing, but write critical logic and security-sensitive code myself.
