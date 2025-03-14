# Challenge Name
# Red Team Agent: Bid Assurance At Source

**Summary**

The challenge is to establish a LLM for a “Red Team” agent that uses a predefined list of
client personas to provide “assurance at source” by indicating the quality of a bid proposal to
those creating it before it is submitted to the customer organisation

**Pain Points**

A Red Team that better represents the client voice rather than opinions from internal
colleagues from the bidder’s organisation
Red Team feedback provided in minutes rather than days, and that can be repeated on
second and final drafts.
Better written proposals are easier for a buyer in the customer organisation to review
Elimination of poor proposal content that is repeatedly submitted by bidders

**Personas**

As Bid Manager, I want to quicker feedback on my draft proposal content that better
represents the feedback that the client would provide after it is submitted. The feedback
helps me improve the quality of my bid.
As Buyer/Evaluator in the customer organisation, I want to receive proposals that are free of
errors, that answer the questions as intended and are easy to read and evaluate. Better
quality bids should enable us to identify genuine differences in the solution being offered
rather than how well the solution has been described.

**Business Context**

_Assurance: concept and challenges_

Project assurance is the process of providing confidence to stakeholders that projects will achieve
their scope, time, cost and quality objectives, and realise their benefits.
In an assurance context a stakeholder is anyone who delegates work to another person/team –
whether it is assigned to their own team or to a third party, possibly through a contract – or any
parties who will benefit or be impacted by the work being completed as intended.
Stakeholders seek confidence through a number of means. But in essence that the person/team
undertaking the work are:
competent for the complexity/nature of the work;
using methods and techniques appropriate for the complexity/nature of the work;
providing updates on their actions, decisions, current status and forecasts.
Confidence is enhanced when competency, methods and techniques are certified as being fit for
purpose – for example a pilot holds a valid licence for the type of aircraft they are piloting and that
the pre-flight procedures they follow are from an approved and up to date operating manual for the
aircraft and airport. Confidence is further enhanced when there are independent checks – for
example through quality controls, internal/external audit and regulators. A series of checks are often
referred to as “three lines of defence” with the first line responsibility falling to the person/team
undertaking the work and each subsequent line providing additional degrees of independence.
However, there are numerous challenges of project assurance, which can include:
when these independent checks become burdensome in terms of effort and duration – either to
the person/team undertaking the checks or to the person/team being checked
the checks are inadequate and provide a false level of confidence (too high or too low);
the checks identify issues that are not material to the satisfactory completion of the delegated
work, but nevertheless prompt changes or rework and therefore introduce new risks;
the checks are completed too late in the process not giving sufficient time to resolve any issues
prior to when the work should otherwise be completed.
Much of these issues stem from assurance being primarily an event-based and manual activity – i.e.
people turning up to ask questions and gather evidence in support of a scheduled decision that needs
to be made. New concepts emerging from AI/data analytics enabled assurance is an approach of
“always-on” assurance, akin to the back box that newly qualified drivers have for their insurance, and
“assurance at source” akin to lane departure warning systems that modern cars have as driving aids.

_“Red Team” in assurance: concepts and challenges_

In the military a ‘Red Team’ is a group that simulates adversarial actions to test the effectiveness of
strategies and personnel.
In a bidding context, bidders often establish Red Teams to review their draft proposals from the
perspective of the customer to independently critique the content and provide feedback to the bid
team on where they can improve.
The challenge is that the Red Team members are typically people who work for the same organisation
as the bid team and are generally fellow sales or delivery personnel. They are not necessarily like the
buyers/evaluators in the customer organisation they attempt to emulate.
Project:Hack24.05 Writeup 21/02/25 Page 3 of 5

_The Red Team Agent_

The concept of this challenge is for a client organisation to create a custom GPT as a Red Team agent
which the client provides to bidders alongside the Request For Proposal (RFP) documentation. The
goal is to help bidders improve their bids and/or help them make their bid go/no-go decision.
Receiving better quality bids is valuable to the buyer in the customer organisation as it enables them
to better assess the bids on the merit of their offer rather than on the quality of their bid writing.
The Red Team Agent will provide feedback on draft proposal based on the specific set of
documentation for the RFP and from applying a range of client roles who would usually review
proposals, e.g. Procurement officers, finance managers, legal/commercial specialists, SRO/project
owner, social value specialists, sustainability specialists, client project manager.
It is important that the Red Team agent only provides feedback on draft proposal content. It should
not produce proposal content.
While the primary focus is on client organisations, the solution should also be organisation-agnostic
and applicable to the bid creation process.

**Dataset Description**

The key to the successful development of the Red Team Agent is gaining feedback from buyers on
what they look for in good bid submissions and things they would like bidders to avoid doing. We have
provided some transcripts from interviews with buyers for this purpose, but don’t be limited by this
and consider other ways to train the Red Team Agent.

Teams will be provided with:
- Transcripts from interviews with a range of bid evaluators from buyer organisations to establish
the foundation for agent perspectives.
- Commercial/legal specialist
- Social value specialist
- Environmental sustainability specialist
- Project manager
- Technical manager
- Business manger (relating to the solution being procured)
·Synthetic procurement and proposal documents:
-Client RFP documentation

Participants will need to develop an agent(s) capable of reviewing draft proposal content to
generate feedback to help bid teams refine and improve the quality of their proposal.

**Success Criteria**

A successful solution will include:
An LLM powered agent designed to assume the role of a Red Team.
A system that allows an agent to review proposal content in context of a specific RFP
and generate structured feedback.
A user-friendly method of presenting agent reports—consider how decision-makers will
consume and act upon the output.
A focus on highlighting key information that facilitates effective decision-making by the
bid team regarding how to improve their proposal content.
Guardrails to prevent bidders instructing the agent to produce content for them (it should
be limited to providing a critique only).
Project:Hack24.05 Writeup 21/02/25 Page 4 of 5
Also consider how this agent could be further developed in future Hacks, for example:
·using agentic workflow so that it forms just one part of the bid writing process. In that
scenarios what other agents could be developed (possibly by the bidding organisations) that
it could be linked to.
a client agent to review/test their Request for Proposal (RFP) packs before they are
published – checking for inconsistencies or weakness/non-compliance against
procurement guidelines or good practice.
could prospective bidders be allowed to further develop it to assess how well their winthemes are threaded through a set of responses (i.e. rather than feedback on a draft
response to a specific question) or would that be better developed as a separate Agent?

**Benefit**

This challenge presents an opportunity to enhance both the bid creation process for bidders
and, in turn, the bid review process for client organisations (and main contractors seeking
tenders from their supply chains), improving the quality proposals submitted.
This challenge holds the benefit of introducing a whole new approach to “assurance at
source”. With custom agents bid teams can receive near instantaneous feedback to refine
their proposals and clients can receive proposals that are better presented reducing making
it easier to identify the best bidder with less effort.


**Useful Resources**

_LLM development_

A potential tool for teams to explore is https://lmstudio.ai/, which enables secure local
deployment of LLMs, increasing the practicality and scalability of any solution developed.
Proposal management good practice

_Tips for persuasive writing_

https://winningthebusiness.com/apmp-best-practices-101-writing-persuasively/
Crown commercial services guidance

_How to evaluate proposals_

https://www.crowncommercial.gov.uk/news/how-to-evaluate-bids-procurement-essentials

_Evaluation guidance_

https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/987130/Bid_evaluation_guidance_note_May_2021.pdf
