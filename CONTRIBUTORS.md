# A Git Style Guide


## Merge Request

### Title
`<ticket_number>: <ticket_title>`. Examples: `JP-4: Add contributors guide`.

### Description
Description should be human readable. Bullet points of changes should be added.

```
Added Ansible role for Static Frontend
- role-static-frontend
- tests
- instruction on how to use
```
If you know who need to pay special attention (e.g. team lead, architect, etc), add mention in to Description:

```
@azhitnik, @tavor118, @all
```

### Other Rules
1. If your PR is not ready for merge, add `WIP:` prefix. This is Work In Progress.
2. If the feature branch is in conflict with the target branch, it is necessary to rebase, and only then merge.
3. Ensure that everybody aware of your PR. Notify about your PR your teammates.
4. By convention approve form your mentor means that PR request is safe for merge.
5. By convention any unresolved discussion is blocker for merge. It is up to you to ensure all of discussions are resolved. Please be pushy if somebody doesn't respond in discussions, or don't resolve. Escalate if needed.
6. Your pull request should be on top of HEAD. Please check it periodically and ensure that PR is properly rebased.

__NOTE:__ This is your responsibility as a developer to make everything so that PR is got accepted. Ask, push, escalate.


## Branching

### Branch Naming
Gitflow by default, 

| Branch | Purpose | Rule | Example |
| ------ | ------- | ---- | ------- |
| Feature | New features, tasks, etc. | `feature/<ticket_number>-<short-title>` | `feature/JP-1504-add-ansible-role` |
| Feature (No task) | In __exceptional cases__, it is possible to create branches without task assigned. | feature/<short-title> | `feature/something-important` | 
| Fix/bug/etc | Fixes/bugs | `fix/<ticket_number>-<short-title>` | `fix/JP-2342-hsts` |
| Fix (Not task) | In __exceptional cases__, ad-hock fixes/bugs | `fix/<short-title>` | `fix/super-important-fix` |
| Prototypes (Team) | If something is not planed to be merged | `proto/<short-title>` | `proto/additional-databases` |
| Prototypes (User) | If something is not planed to be merged | `dkurk/<short-title>` | `dkurk/pcas-authentication` |


___
# A Python Style Guide

## Style Guide for Python Code

### Indentation
Use 4 spaces per indentation level.

### Maximum Line Length
Limit all lines to a maximum of 120 characters.
PEP8 recommends to use 79 symbols, but it's not necessary if you use Django.

### Blank Lines
1. Surround top-level function and class definitions with two blank lines.
2. Method definitions inside a class are surrounded by a single blank line.

### Source File Encoding
A code should always use UTF-8.

### Naming
1. Use `lower_case_with_underscores` for packages/modules/functions/methods/variables.
2. Use `UPPER_CASE_WITH_UNDERSCORES` for constants.
3. Use `CamelCase` for classes/exceptions.

## Module Version Numbers
PEP 386, PEP 396


___
# Versioning Specification
Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
