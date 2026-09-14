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
| BUG-07 | A remaining-minutes report still counts work that is already completed. | A test mixes completed and unfinished tasks. |
| BUG-08 | Completion percentage is too low when a planner contains completed and unfinished tasks. | A test verifies an exact percentage. |
| BUG-09 | A longest-task report selects the shortest duration instead. | A test compares at least two different durations. |
| BUG-10 | An earliest-due report selects the latest date instead. | A test compares at least two distinct due dates. |
| BUG-11 | The unfinished-task filter returns completed tasks too. | A test mixes both completion states. |
| BUG-12 | A task exactly at a requested duration threshold is absent from the result. | A test covers equality at the threshold. |
| BUG-13 | Filtering by a priority works only with exact capitalization and spacing. | A test uses a padded, differently cased priority. |
| BUG-14 | Date ordering shows later tasks before earlier ones. | A test covers multiple dates and stable equal-date ordering. |
| BUG-15 | A zero-minute task is treated as valid input. | A test covers zero and a positive duration. |
| BUG-16 | Validation rejects a known priority when its input has case or spacing differences. | A test uses a normalized equivalent of a known priority. |
| TEST-02 | Empty-input behavior of the reporting helpers has no focused direct coverage. | Add concise tests for the documented empty results. |
| TEST-03 | Equal due dates have no direct stability test in the date-ordering helper. | Add a focused no-production-change test. |
| DOC-02 | Contributors need a short map from task-card type to an appropriate PR shape. | Add an accurate guide update only. |
| DOC-03 | The contribution guide lacks a compact reviewer-readiness checklist. | Add a documentation-only checklist. |

For a code card, a strong PR usually contains one regression test and the smallest corresponding production change.

