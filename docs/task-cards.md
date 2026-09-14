# Contribution cards

These cards are deliberately small. An open GitHub issue is the source of truth when one exists; cards give a quick overview without prescribing a patch.

| Card | Symptom to investigate | Suggested acceptance evidence |
| --- | --- | --- |
| BUG-01 | Searching for a task works only when the query uses the title's exact capitalization. | A test covers different case and surrounding spaces. |
| BUG-02 | A task due on the final day of a requested range is absent from the result. | A test covers both range boundaries. |
| BUG-03 | A summary's average duration is unexpectedly low for a populated planner. | A test verifies a planner containing multiple durations. |
| BUG-04 | The task list shows low-priority work before high-priority work. | A test proves the documented priority order and stable ties. |
| BUG-05 | A CSV file cannot reliably round-trip a task title containing commas or quotes. | A test round-trips punctuation-rich title text. |
| BUG-06 | Adding a task with an existing ID silently changes earlier data. | A test preserves the original task and verifies the reported error. |
| TEST-01 | The public behavior rules have no direct test for stable priority ties. | Add a focused test; no production change is necessary if it passes. |
| DOC-01 | The quick-start guide could include an example of running a single test module. | Update the guide and keep documentation links valid. |

For a code card, a strong PR usually contains one regression test and the smallest corresponding production change.
