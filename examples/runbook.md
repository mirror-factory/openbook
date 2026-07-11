## Cover

**Title:** Operating the Nightly Deploy
**Subtitle:** The pipeline, its three buttons, and what to do when a deploy goes quiet
**Format:** Runbook
**Author:** An overnight agent (OpenBook example)
**When:** The morning the pipeline went live

## The sixty-second version

The nightly deploy builds the application, runs the test suite, and ships the result to the fleet at 2am. It runs itself; you only touch it when you want an off-schedule deploy, when you want to hold a night's release, or when something looks wrong in the morning. This document is the whole of what you need for those three moments. If instead you want to know why the pipeline is shaped this way, that story lives in the report that shipped with it; this is only how to drive.

## The buttons

**deploy-now, in the repository's Actions tab.** Builds and ships from the main branch immediately instead of waiting for 2am. Costs a fleet restart during working hours; the fleet drains connections first, so users see nothing, but background jobs pause for about a minute.

**hold-tonight, in the same tab.** Skips the next scheduled deploy only. Nothing builds, nothing ships, and the schedule resumes the following night. Safe to press any time; pressing it twice does not skip two nights.

**rollback, in the same tab, with a typed confirmation.** Reships the previous night's build over the current one. This is the only button that moves the fleet backward; it asks you to type ROLLBACK because it undoes a release users may already depend on.

## Procedures

### Ship a fix before tonight

1. Merge the fix to the main branch; you should see the merge commit on the branch page.
2. Open Actions, choose deploy-now, press Run workflow; you should see a new run appear within a few seconds.
3. Watch the run's final step; it prints the version it shipped and the fleet's post-deploy health check. Green plus a version number is done.

### Hold a risky night

1. Open Actions, choose hold-tonight, press Run workflow.
2. Confirm the run completes; its only step prints the date being skipped.
3. Nothing else is required; tomorrow's 2am deploy resumes on its own.

### Roll back a bad release

1. Open Actions, choose rollback, press Run workflow, and type ROLLBACK in the confirmation box; anything else refuses and exits.
2. The run prints the version it is restoring before it acts; check that this is the version you expect.
3. Watch the final health check as with any deploy. Then write down what was wrong with the rolled-back build while it is fresh; the pipeline cannot do that part.

## When it looks wrong

**The morning fleet is on yesterday's version and nobody pressed hold.** Open the 2am run in Actions; a red build or test step means the deploy refused to ship a broken build, which is it working. The failing step's log names the test or error.

**deploy-now sits queued and never starts.** A previous run is still holding the deploy lock. Open the run list; if the older run is hung rather than working, cancel it and the queued run proceeds.

**The health check failed after a ship.** The fleet kept the old version; the deploy does not cut over on a red check. The check's log names the failing endpoint. Nothing needs undoing; fix forward and press deploy-now.

**Rollback refused your confirmation.** It only accepts the exact word ROLLBACK. That is the guard doing its job, not a bug.

## Appendix

- Workflows: deploy-now, hold-tonight, rollback, in the repository's Actions tab; the 2am schedule lives in the deploy workflow's cron line.
- The deploy lock and its timeout: documented at the top of the deploy workflow file.
- The report that shipped with this pipeline explains its design and records its first honest failures.
- Nothing in this example refers to a real system; the pattern is the content.
