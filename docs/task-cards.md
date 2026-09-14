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
| DOC-02 | Contributors need a compact map of the exercise-helper modules and their responsibilities. | Add an accurate documentation-only module map. |
| DOC-03 | The contribution guide lacks a compact reviewer-readiness checklist. | Add a documentation-only checklist. |
| BUG-17 | A completed-task count reports unfinished work instead. | A mixed completion-state test verifies the count. |
| BUG-18 | Completed minutes omit the work that has been completed. | A test mixes completed and open durations. |
| BUG-19 | Total planned minutes behaves like a single-task value instead of a total. | A test uses two different durations. |
| BUG-20 | A mixed collection is treated as fully completed. | A test contains both a completed and an open task. |
| BUG-21 | The unfinished-task helper selects the last open task rather than the first. | A test uses two unfinished tasks around a completed one. |
| BUG-22 | A mixed completion state is displayed as complete. | A test covers the `in progress` state. |
| BUG-23 | A past due date loses its negative day offset. | A test uses a date two days before the reference date. |
| BUG-24 | A task due today is classified as overdue. | A test uses equal due and reference dates. |
| BUG-25 | Filtering for one date returns tasks from other dates. | A test includes tasks due on two different dates. |
| BUG-26 | A month filter mixes tasks from the same month in different years. | A test uses the same month across two years. |
| BUG-27 | The next-due helper includes a task on the reference day. | A test includes tasks due today and tomorrow. |
| BUG-28 | Weekday count excludes the final requested date. | A test covers an inclusive Monday-to-Tuesday range. |
| BUG-29 | Saturday is not considered a weekend. | A test covers both weekend days. |
| BUG-30 | A duration over an hour shows the wrong remaining minutes. | A test formats 75 minutes. |
| BUG-31 | Completion markers are inverted in a formatted task line. | A test covers an open and a completed task. |
| BUG-32 | A shortened title exceeds its requested display limit. | A test uses a valid limit of at least three, an ellipsized title, and a title that already fits. |
| BUG-33 | High and low priority symbols are swapped. | A test verifies all documented symbols. |
| BUG-34 | Zero tasks is written using the singular form. | A test covers zero, one, and multiple tasks. |
| BUG-35 | A zero-day due offset is labeled overdue. | A test covers negative, zero, and positive offsets. |
| BUG-36 | Requesting the first zero tasks returns tasks anyway. | A test covers a zero limit. |
| BUG-37 | Chunking drops the final incomplete group. | A test chunks three tasks with a size of two. |
| BUG-38 | Unique priorities are reordered instead of preserving first appearance. | A test uses repeated priorities in a non-alphabetical order. |
| BUG-39 | Replacing a task changes its list position. | A test replaces the first of two tasks. |
| BUG-40 | Removing a task ID retains the removed task instead of the others. | A test removes one of two IDs. |
| BUG-41 | A zero-based task slice begins one item too late. | A test verifies a nonzero offset and one-item limit. |
| BUG-42 | Grouping by due date loses earlier tasks that share a date. | A test uses two tasks with one due date. |
| BUG-43 | Priority minute totals keep only the last task for a priority. | A test sums two tasks with one priority and one with another. |
| BUG-44 | Retitling a task mutates the original task. | A test verifies independent identity and unchanged original title. |
| BUG-45 | A task record turns its completion value into text. | A test checks that the record value remains a boolean. |
| BUG-46 | Reading a record fails when optional completion data is absent. | A test builds a task from a minimal record. |
| BUG-47 | An even-sized median selects one middle duration rather than their average. | A test uses two different durations. |

For a code card, a strong PR usually contains one regression test and the smallest corresponding production change.

