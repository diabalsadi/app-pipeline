# Validation checklist

Run every check. Each failure becomes a row in the "Open issues" table.

## Coverage
- [ ] Every first-version feature (F1, F2, …) has at least one user story.
- [ ] Every user story appears on at least one screen.
- [ ] Every screen serves at least one story, or is a standard screen (welcome, settings, error).
- [ ] Every story has acceptance criteria that a tester could check without asking anyone.

## Missing flows
- [ ] Sign up, sign in, sign out, and password reset (or a sign-in method that removes passwords).
- [ ] Deleting an account and its data, which app stores require when an app has accounts.
- [ ] Empty states: what each list or dashboard shows before there is any data.
- [ ] Error states: no connection, a failed payment, a form with invalid input.
- [ ] Loading states for anything that waits on the network.
- [ ] Notifications: what triggers them, and how a user turns them off.
- [ ] Admin or moderation needs, if users create content or there is more than one role.
- [ ] Payment flows end to end, if the app takes money: purchase, receipt, refund, and cancelling a subscription.

## Consistency
- [ ] No two stories contradict each other, such as "anyone can view" and "only members can view".
- [ ] Roles in the stories match the roles table.
- [ ] Platform needs match the business plan. A phone-first idea with desktop-only stories is a contradiction.
- [ ] Success metrics in the business plan can be measured, so something records the events they need.

## Scope
- [ ] The Must stories can deliver the main task from the business plan on their own.
- [ ] Nothing in Must depends on a Later story.
- [ ] The first version has no more than about 12 Must screens. If it has more, recommend a cut.

## Sensitive areas
- [ ] Personal data collected is listed, with a reason for each item.
- [ ] Payments, health data, users under 16, and location each have a story that covers consent or compliance, where they apply.
