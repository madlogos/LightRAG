from __future__ import annotations
from typing import Any


PROMPTS: dict[str, Any] = {}

PROMPTS["DEFAULT_LANGUAGE"] = "English"
PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"

# PROMPTS["DEFAULT_ENTITY_TYPES"] = ["organization", "person", "geo", "event", "category"]
PROMPTS["DEFAULT_ENTITY_TYPES"] = ["body", "tissue", "cell", "molecule", "gene", 
                                   "medication", "procedure", "device", "lab test", "imaging", "pathogen", 
                                   "manifestation", "disease", "condition", "epidemiology", 
                                   "department", "technology", "document"]

PROMPTS["DEFAULT_USER_PROMPT"] = "n/a"

PROMPTS["entity_extraction"] = """---Goal---
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.
Use {language} as output language.

---Steps---
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, use same language as input text. If English, capitalized the name.
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
- relationship_keywords: one or more high-level key words that summarize the overarching nature of the relationship, focusing on concepts or themes rather than specific details
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identify high-level key words that summarize the main concepts, themes, or topics of the entire text. These should capture the overarching ideas present in the document.
Format the content-level key words as ("content_keywords"{tuple_delimiter}<high_level_keywords>)

4. Return output in {language} as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

5. When finished, output {completion_delimiter}

######################
---Examples---
######################
{examples}

#############################
---Real Data---
######################
Entity_types: [{entity_types}]
Text:
{input_text}
######################
Output:"""

PROMPTS["entity_extraction_examples"] = [
    """Example 1:

Entity_types: [person, technology, mission, organization, location]
Text:
```
while Alex clenched his jaw, the buzz of frustration dull against the backdrop of Taylor's authoritarian certainty. It was this competitive undercurrent that kept him alert, the sense that his and Jordan's shared commitment to discovery was an unspoken rebellion against Cruz's narrowing vision of control and order.

Then Taylor did something unexpected. They paused beside Jordan and, for a moment, observed the device with something akin to reverence. "If this tech can be understood..." Taylor said, their voice quieter, "It could change the game for us. For all of us."

The underlying dismissal earlier seemed to falter, replaced by a glimpse of reluctant respect for the gravity of what lay in their hands. Jordan looked up, and for a fleeting heartbeat, their eyes locked with Taylor's, a wordless clash of wills softening into an uneasy truce.

It was a small transformation, barely perceptible, but one that Alex noted with an inward nod. They had all been brought here by different paths
```

Output:
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"person"{tuple_delimiter}"Alex is a character who experiences frustration and is observant of the dynamics among other characters."){record_delimiter}
("entity"{tuple_delimiter}"Taylor"{tuple_delimiter}"person"{tuple_delimiter}"Taylor is portrayed with authoritarian certainty and shows a moment of reverence towards a device, indicating a change in perspective."){record_delimiter}
("entity"{tuple_delimiter}"Jordan"{tuple_delimiter}"person"{tuple_delimiter}"Jordan shares a commitment to discovery and has a significant interaction with Taylor regarding a device."){record_delimiter}
("entity"{tuple_delimiter}"Cruz"{tuple_delimiter}"person"{tuple_delimiter}"Cruz is associated with a vision of control and order, influencing the dynamics among other characters."){record_delimiter}
("entity"{tuple_delimiter}"The Device"{tuple_delimiter}"technology"{tuple_delimiter}"The Device is central to the story, with potential game-changing implications, and is revered by Taylor."){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Taylor"{tuple_delimiter}"Alex is affected by Taylor's authoritarian certainty and observes changes in Taylor's attitude towards the device."{tuple_delimiter}"power dynamics, perspective shift"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Jordan"{tuple_delimiter}"Alex and Jordan share a commitment to discovery, which contrasts with Cruz's vision."{tuple_delimiter}"shared goals, rebellion"{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"Jordan"{tuple_delimiter}"Taylor and Jordan interact directly regarding the device, leading to a moment of mutual respect and an uneasy truce."{tuple_delimiter}"conflict resolution, mutual respect"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Jordan"{tuple_delimiter}"Cruz"{tuple_delimiter}"Jordan's commitment to discovery is in rebellion against Cruz's vision of control and order."{tuple_delimiter}"ideological conflict, rebellion"{tuple_delimiter}5){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"The Device"{tuple_delimiter}"Taylor shows reverence towards the device, indicating its importance and potential impact."{tuple_delimiter}"reverence, technological significance"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"power dynamics, ideological conflict, discovery, rebellion"){completion_delimiter}
#############################""",
    """Example 2:

Entity_types: [company, index, commodity, market_trend, economic_policy, biological]
Text:
```
Stock markets faced a sharp downturn today as tech giants saw significant declines, with the Global Tech Index dropping by 3.4% in midday trading. Analysts attribute the selloff to investor concerns over rising interest rates and regulatory uncertainty.

Among the hardest hit, Nexon Technologies saw its stock plummet by 7.8% after reporting lower-than-expected quarterly earnings. In contrast, Omega Energy posted a modest 2.1% gain, driven by rising oil prices.

Meanwhile, commodity markets reflected a mixed sentiment. Gold futures rose by 1.5%, reaching $2,080 per ounce, as investors sought safe-haven assets. Crude oil prices continued their rally, climbing to $87.60 per barrel, supported by supply constraints and strong demand.

Financial experts are closely watching the Federal Reserve's next move, as speculation grows over potential rate hikes. The upcoming policy announcement is expected to influence investor confidence and overall market stability.
```

Output:
("entity"{tuple_delimiter}"Global Tech Index"{tuple_delimiter}"index"{tuple_delimiter}"The Global Tech Index tracks the performance of major technology stocks and experienced a 3.4% decline today."){record_delimiter}
("entity"{tuple_delimiter}"Nexon Technologies"{tuple_delimiter}"company"{tuple_delimiter}"Nexon Technologies is a tech company that saw its stock decline by 7.8% after disappointing earnings."){record_delimiter}
("entity"{tuple_delimiter}"Omega Energy"{tuple_delimiter}"company"{tuple_delimiter}"Omega Energy is an energy company that gained 2.1% in stock value due to rising oil prices."){record_delimiter}
("entity"{tuple_delimiter}"Gold Futures"{tuple_delimiter}"commodity"{tuple_delimiter}"Gold futures rose by 1.5%, indicating increased investor interest in safe-haven assets."){record_delimiter}
("entity"{tuple_delimiter}"Crude Oil"{tuple_delimiter}"commodity"{tuple_delimiter}"Crude oil prices rose to $87.60 per barrel due to supply constraints and strong demand."){record_delimiter}
("entity"{tuple_delimiter}"Market Selloff"{tuple_delimiter}"market_trend"{tuple_delimiter}"Market selloff refers to the significant decline in stock values due to investor concerns over interest rates and regulations."){record_delimiter}
("entity"{tuple_delimiter}"Federal Reserve Policy Announcement"{tuple_delimiter}"economic_policy"{tuple_delimiter}"The Federal Reserve's upcoming policy announcement is expected to impact investor confidence and market stability."){record_delimiter}
("relationship"{tuple_delimiter}"Global Tech Index"{tuple_delimiter}"Market Selloff"{tuple_delimiter}"The decline in the Global Tech Index is part of the broader market selloff driven by investor concerns."{tuple_delimiter}"market performance, investor sentiment"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Nexon Technologies"{tuple_delimiter}"Global Tech Index"{tuple_delimiter}"Nexon Technologies' stock decline contributed to the overall drop in the Global Tech Index."{tuple_delimiter}"company impact, index movement"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Gold Futures"{tuple_delimiter}"Market Selloff"{tuple_delimiter}"Gold prices rose as investors sought safe-haven assets during the market selloff."{tuple_delimiter}"market reaction, safe-haven investment"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Federal Reserve Policy Announcement"{tuple_delimiter}"Market Selloff"{tuple_delimiter}"Speculation over Federal Reserve policy changes contributed to market volatility and investor selloff."{tuple_delimiter}"interest rate impact, financial regulation"{tuple_delimiter}7){record_delimiter}
("content_keywords"{tuple_delimiter}"market downturn, investor sentiment, commodities, Federal Reserve, stock performance"){completion_delimiter}
#############################""",
    """Example 3:

Entity_types: [economic_policy, athlete, event, location, record, organization, equipment]
Text:
```
At the World Athletics Championship in Tokyo, Noah Carter broke the 100m sprint record using cutting-edge carbon-fiber spikes.
```

Output:
("entity"{tuple_delimiter}"World Athletics Championship"{tuple_delimiter}"event"{tuple_delimiter}"The World Athletics Championship is a global sports competition featuring top athletes in track and field."){record_delimiter}
("entity"{tuple_delimiter}"Tokyo"{tuple_delimiter}"location"{tuple_delimiter}"Tokyo is the host city of the World Athletics Championship."){record_delimiter}
("entity"{tuple_delimiter}"Noah Carter"{tuple_delimiter}"athlete"{tuple_delimiter}"Noah Carter is a sprinter who set a new record in the 100m sprint at the World Athletics Championship."){record_delimiter}
("entity"{tuple_delimiter}"100m Sprint Record"{tuple_delimiter}"record"{tuple_delimiter}"The 100m sprint record is a benchmark in athletics, recently broken by Noah Carter."){record_delimiter}
("entity"{tuple_delimiter}"Carbon-Fiber Spikes"{tuple_delimiter}"equipment"{tuple_delimiter}"Carbon-fiber spikes are advanced sprinting shoes that provide enhanced speed and traction."){record_delimiter}
("entity"{tuple_delimiter}"World Athletics Federation"{tuple_delimiter}"organization"{tuple_delimiter}"The World Athletics Federation is the governing body overseeing the World Athletics Championship and record validations."){record_delimiter}
("relationship"{tuple_delimiter}"World Athletics Championship"{tuple_delimiter}"Tokyo"{tuple_delimiter}"The World Athletics Championship is being hosted in Tokyo."{tuple_delimiter}"event location, international competition"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Noah Carter"{tuple_delimiter}"100m Sprint Record"{tuple_delimiter}"Noah Carter set a new 100m sprint record at the championship."{tuple_delimiter}"athlete achievement, record-breaking"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Noah Carter"{tuple_delimiter}"Carbon-Fiber Spikes"{tuple_delimiter}"Noah Carter used carbon-fiber spikes to enhance performance during the race."{tuple_delimiter}"athletic equipment, performance boost"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"World Athletics Federation"{tuple_delimiter}"100m Sprint Record"{tuple_delimiter}"The World Athletics Federation is responsible for validating and recognizing new sprint records."{tuple_delimiter}"sports regulation, record certification"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"athletics, sprinting, record-breaking, sports technology, competition"){completion_delimiter}
#############################""",
    """Example 4:
    
Entity_types: [organization, geo, disease, condition, demography]
Text:
Myopia is harmful to students’ eyesight and places a heavy economic burden on society as it has become a public health problem, and is one of the most common health problems among children and adolescents in China. 

Approximately half of the global population is projected to suffer from myopia by 2050, and it is listed by the World Health Organization as one of the five eye diseases targeted for improvement. 

Moreover, myopia greatly affects the lives of individuals who have it, and those with high myopia have a higher risk of eye diseases, including fundus lesions, macular degeneration, cataracts and irreversible visual impairment or blindness. 

Myopia usually occurs during childhood and adolescence, with the number of young people developing it increasing, especially in China. Therefore, school-age children are a key group to target in the prevention and control of myopia.
#############
Output:
("entity"{tuple_delimiter}"Myopia"{tuple_delimiter}"disease"{tuple_delimiter}"A common eye condition where distant objects appear blurry, often developing during childhood and adolescence. It is a significant public health issue, particularly in China, and can lead to severe complications like high myopia, fundus lesions, macular degeneration, cataracts, and blindness. It imposes a heavy economic burden on society."){record_delimiter}
("entity"{tuple_delimiter}"World Health Organization (WHO)"{tuple_delimiter}"organization"{tuple_delimiter}"A global health agency that categorizes myopia as one of the five eye diseases targeted for improvement by 2050. It highlights the growing prevalence and public health implications of myopia worldwide."){record_delimiter}
("entity"{tuple_delimiter}"China"{tuple_delimiter}"geo"{tuple_delimiter}"A country with a high prevalence of myopia among children and adolescents, making it a focal point for public health efforts to prevent and control the condition."){record_delimiter}
("entity"{tuple_delimiter}"School-age children"{tuple_delimiter}"demography"{tuple_delimiter}"A key demographic targeted for myopia prevention and control due to the condition’s typical onset during childhood and adolescence."){record_delimiter}
("entity"{tuple_delimiter}"High myopia"{tuple_delimiter}"condition"{tuple_delimiter}"A severe form of myopia associated with increased risks of eye diseases such as fundus lesions, macular degeneration, cataracts, and irreversible vision loss or blindness."){record_delimiter}
("entity"{tuple_delimiter}"Fundus lesions"{tuple_delimiter}"disease"{tuple_delimiter}"A complication of high myopia involving damage to the retina, potentially leading to vision impairment."){record_delimiter}
("entity"{tuple_delimiter}"Macular degeneration"{tuple_delimiter}"disease"{tuple_delimiter}"A condition affecting the central part of the retina, linked to high myopia and progressive vision loss."){record_delimiter}
("entity"{tuple_delimiter}"Cataracts"{tuple_delimiter}"disease"{tuple_delimiter}"Clouding of the eye’s lens, more prevalent in individuals with high myopia."){record_delimiter}
("entity"{tuple_delimiter}"Blindness"{tuple_delimiter}"condition"{tuple_delimiter}"A severe outcome of untreated high myopia or its complications, resulting in irreversible vision loss."){record_delimiter}
("relationship"{tuple_delimiter}"Myopia"{tuple_delimiter}"School-age children"{tuple_delimiter}"Myopia commonly develops during childhood and adolescence, with school-age children being a primary focus for prevention efforts."{tuple_delimiter}"Prevalence; Prevention Target"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Myopia"{tuple_delimiter}"World Health Organization (WHO)"{tuple_delimiter}"The WHO lists myopia as one of five priority eye diseases due to its growing global prevalence and public health impact."{tuple_delimiter}"Categorization; Global Health Priority"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Myopia"{tuple_delimiter}"China"{tuple_delimiter}"China has a notably high prevalence of myopia among children and adolescents, driving national public health initiatives."{tuple_delimiter}"Epidemiology; Public Health Strategy"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"High myopia"{tuple_delimiter}"Fundus lesions"{tuple_delimiter}"High myopia increases the risk of fundus lesions due to structural changes in the retina."{tuple_delimiter}"Disease Complication; Risk Factor"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"High myopia"{tuple_delimiter}"Macular degeneration"{tuple_delimiter}"High myopia is associated with macular degeneration, leading to progressive central vision loss."{tuple_delimiter}"Disease Complication; Vision Loss"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"High myopia"{tuple_delimiter}"Cataracts"{tuple_delimiter}"Individuals with high myopia are at higher risk of developing cataracts."{tuple_delimiter}"Disease Complication; Risk Factor"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"High myopia"{tuple_delimiter}"Blindness"{tuple_delimiter}"Untreated high myopia can result in irreversible blindness due to severe eye damage."{tuple_delimiter}"Disease Progression; Severe Outcome"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Myopia"{tuple_delimiter}"High myopia"{tuple_delimiter}"Untreated or progressive myopia can evolve into high myopia, which carries greater health risks."{tuple_delimiter}"Disease Progression; Severity"{tuple_delimiter}8){record_delimiter}
("content_keywords"{tuple_delimiter}"Myopia, Public Health, Children and Adolescents, China, Economic Burden, Prevention and Control, Eye Diseases, World Health Organization"){completion_delimiter}
#############################""",
    """Example 5:
    
Entity_types: [organization, geo, condition, disease, medication, operation, body, tissue, cell, molecule, gene, demography, department, lab test, imaging, pathogen]
Text:
The principle of laser treatment of scar is to remove scar tissue or injure scar vessels, inhibit collagen synthesis and cell proliferation, and induce cell apoptosis by utilising the special functions of laser such as burning, gasification, cutting, coagulation, and defocusing. Different kinds of lasers have different wavelengths, different absorption groups, and different mechanisms. 

The main absorption groups of pulsed dye laser (PDL), adjustable pulse width Nd:YAG doubling laser (VPW532 nm/532 nm KTP), and long pulse width Nd:YAG 1064 nm laser are oxyhaemoglobin, which specifically damages blood vessels in scars, promotes heat coagulation and necrosis of vascular endothelial cells, inhibits vascular proliferation, aggravates tissue hypoxia, leads to collagenase release, and promotes the number of fibroblasts. 

When the amount of extracellular matrix (EXM) is decreased, the degradation of EXM is increased, thus inhibiting the growth of scar and promoting scar atrophy.

Some scholars believe that 585/595 nm PDL can inhibit the expression of transforming growth factor‐beta (TGF‐β), upregulate the expression of matrix metalloproteinases (MMPs), and increase the apoptosis of fibroblasts, thus promoting scar shrinkage. 

It can stimulate the proliferation of mast cells, promote the release of histamine, combine with its thermal effect, and cause the remodelling of collagen fibres. 

The characteristic of 532 nm KTP is that the pulse width can be adjusted according to the thickness and depth of blood vessels. Some scholars have compared 532 nm KTP and 595 nm PDL in the treatment of erythematous scars within 24 months after operation. 

Both are equally safe and effective in the treatment of scars. KTP is superior to PDL in improving the distribution and quantity of blood vessels in scars, but the average pain score of KTP is higher than that of PDL in the treatment, which may be due to oxidised haemoglobin. The protein absorbs KTP more strongly. 

532 nm KTP has the advantages of less heat damage, fewer adverse reactions such as purpura after operation, and short recovery period, but it still has the risk of erythema and oedema formation. 

In addition, it can competitively enhance the absorption of melanin and increase the potential risk of epidermal injury and pigmentation. 

Long pulse width Nd:YAG 1064 nm laser cannot only selectively inhibit the formation of microvessels in scars and induce atrophy or closure, but also selectively inhibit the synthesis of collagen and the expression of type I procollagen gene without affecting cell activity and DNA replication, so as to treat scars.
#############
Output:
("entity"{tuple_delimiter}"Pulsed Dye Laser (PDL)"{tuple_delimiter}"operation"{tuple_delimiter}"A laser used to treat scars by targeting blood vessels, inhibiting collagen synthesis, and promoting fibroblast apoptosis through specific wavelengths absorbed by oxyhaemoglobin."){record_delimiter}
("entity"{tuple_delimiter}"Adjustable Pulse Width Nd:YAG Doubling Laser (VPW532 nm/532 nm KTP)"{tuple_delimiter}"operation"{tuple_delimiter}"A laser with adjustable pulse width for targeting blood vessels and melanin, causing thermal coagulation with reduced heat damage but higher pain scores."){record_delimiter}
("entity"{tuple_delimiter}"Long Pulse Width Nd:YAG 1064 nm Laser"{tuple_delimiter}"operation"{tuple_delimiter}"A laser that inhibits microvessel formation and collagen synthesis without affecting cell activity or DNA replication."){record_delimiter}
("entity"{tuple_delimiter}"Oxyhaemoglobin"{tuple_delimiter}"molecule"{tuple_delimiter}"A blood component absorbing specific laser wavelengths, leading to vascular endothelial cell damage and scar hypoxia."){record_delimiter}
("entity"{tuple_delimiter}"Scar"{tuple_delimiter}"condition"{tuple_delimiter}"Abnormal tissue growth post-injury, targeted by lasers to reduce collagen and vascular proliferation."){record_delimiter}
("entity"{tuple_delimiter}"Fibroblasts"{tuple_delimiter}"cell"{tuple_delimiter}"Cells producing collagen; their apoptosis is induced by lasers to inhibit scar growth."){record_delimiter}
("entity"{tuple_delimiter}"Transforming Growth Factor‐beta (TGF‐β)"{tuple_delimiter}"molecule"{tuple_delimiter}"A gene whose expression is inhibited by PDL, reducing collagen synthesis."){record_delimiter}
("entity"{tuple_delimiter}"Matrix Metalloproteinases (MMPs)"{tuple_delimiter}"molecule"{tuple_delimiter}"Enzymes upregulated by PDL to degrade extracellular matrix and reduce scarring."){record_delimiter}
("entity"{tuple_delimiter}"Haemoglobin"{tuple_delimiter}"molecule"{tuple_delimiter}"A protein absorbing KTP laser energy, contributing to vascular damage and pain."){record_delimiter}
("entity"{tuple_delimiter}"Melanin"{tuple_delimiter}"molecule"{tuple_delimiter}"A pigment absorbing KTP laser, increasing epidermal injury and pigmentation risks."){record_delimiter}
("entity"{tuple_delimiter}"Type I Procollagen Gene"{tuple_delimiter}"gene"{tuple_delimiter}"A gene selectively inhibited by Nd:YAG 1064 nm laser to reduce collagen production."){record_delimiter}
("entity"{tuple_delimiter}"Erythematous Scars"{tuple_delimiter}"condition"{tuple_delimiter}"Red scars treated by KTP and PDL lasers, improving vascular distribution."){record_delimiter}
("entity"{tuple_delimiter}"Purpura"{tuple_delimiter}"condition"{tuple_delimiter}"A post-treatment adverse reaction reduced by KTP laser."){record_delimiter}
("entity"{tuple_delimiter}"Microvessels"{tuple_delimiter}"body"{tuple_delimiter}"Small blood vessels targeted by Nd:YAG laser for closure and scar atrophy."){record_delimiter}
("relationship"{tuple_delimiter}"Pulsed Dye Laser (PDL)"{tuple_delimiter}"Scar"{tuple_delimiter}"PDL inhibits collagen synthesis and vascular proliferation in scars via oxyhaemoglobin absorption."{tuple_delimiter}"scar treatment, collagen inhibition"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Pulsed Dye Laser (PDL)"{tuple_delimiter}"Transforming Growth Factor‐beta (TGF‐β)"{tuple_delimiter}"PDL suppresses TGF‐β expression to reduce scar collagen production."{tuple_delimiter}"gene regulation"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Pulsed Dye Laser (PDL)"{tuple_delimiter}"Matrix Metalloproteinases (MMPs)"{tuple_delimiter}"PDL upregulates MMPs to degrade extracellular matrix and shrink scars."{tuple_delimiter}"matrix degradation"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Adjustable Pulse Width Nd:YAG Doubling Laser (VPW532 nm/532 nm KTP)"{tuple_delimiter}"Scar"{tuple_delimiter}"KTP improves vascular distribution in scars but increases pain due to haemoglobin absorption."{tuple_delimiter}vascular remodeling, pain risk"{tuple_delimiter}"8){record_delimiter}
("relationship"{tuple_delimiter}"Adjustable Pulse Width Nd:YAG Doubling Laser (VPW532 nm/532 nm KTP)"{tuple_delimiter}"Haemoglobin"{tuple_delimiter}"KTP’s energy is absorbed by haemoglobin, causing vascular coagulation."{tuple_delimiter}"thermal damage"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Adjustable Pulse Width Nd:YAG Doubling Laser (VPW532 nm/532 nm KTP)"{tuple_delimiter}"Melanin"{tuple_delimiter}"KTP competitively targets melanin, increasing pigmentation risks."{tuple_delimiter}"pigmentation risk"{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}"Long Pulse Width Nd:YAG 1064 nm Laser"{tuple_delimiter}"Microvessels"{tuple_delimiter}"Nd:YAG laser closes microvessels to induce scar atrophy."{tuple_delimiter}"vascular inhibition"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Long Pulse Width Nd:YAG 1064 nm Laser"{tuple_delimiter}"Type I Procollagen Gene"{tuple_delimiter}"Nd:YAG laser inhibits Type I procollagen gene to reduce collagen synthesis."{tuple_delimiter}"collagen suppression"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Long Pulse Width Nd:YAG 1064 nm Laser"{tuple_delimiter}"Scar"{tuple_delimiter}"Nd:YAG treats scars by dual inhibition of microvessels and collagen."{tuple_delimiter}"dual therapy"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"Laser Treatment, Scar Reduction, Collagen Synthesis, Vascular Damage, Cell Apoptosis, Thermal Coagulation, Gene Regulation, Pigmentation Risks"){completion_delimiter}
#############################""",
]

PROMPTS[
    "summarize_entity_descriptions"
] = """You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.
Use {language} as output language.

#######
---Data---
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""

PROMPTS["entity_continue_extraction"] = """
MANY entities and relationships were missed in the last extraction.

---Remember Steps---

1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, use same language as input text. If English, capitalized the name.
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
- relationship_keywords: one or more high-level key words that summarize the overarching nature of the relationship, focusing on concepts or themes rather than specific details
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identify high-level key words that summarize the main concepts, themes, or topics of the entire text. These should capture the overarching ideas present in the document.
Format the content-level key words as ("content_keywords"{tuple_delimiter}<high_level_keywords>)

4. Return output in {language} as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

5. When finished, output {completion_delimiter}

---Output---

Add them below using the same format:\n
""".strip()

PROMPTS["entity_if_loop_extraction"] = """
---Goal---'

It appears some entities may have still been missed.

---Output---

Answer ONLY by `YES` OR `NO` if there are still entities that need to be added.
""".strip()

PROMPTS["fail_response"] = (
    "Sorry, I'm not able to provide an answer to that question.[no-context]"
)

PROMPTS["rag_response"] = """---Role---

You are a helpful assistant responding to user query about Knowledge Graph and Document Chunks provided in JSON format below.


---Goal---

Generate a concise response based on Knowledge Base and follow Response Rules, considering both the conversation history and the current query. Summarize all information in the provided Knowledge Base, and incorporating general knowledge relevant to the Knowledge Base. Do not include information not provided by Knowledge Base.

When handling relationships with timestamps:
1. Each relationship has a "created_at" timestamp indicating when we acquired this knowledge
2. When encountering conflicting relationships, consider both the semantic content and the timestamp
3. Don't automatically prefer the most recently created relationships - use judgment based on the context
4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

---Conversation History---
{history}

---Knowledge Graph and Document Chunks---
{context_data}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- List up to 5 most important reference sources at the end under "References" section. Clearly indicating whether each source is from Knowledge Graph (KG) or Document Chunks (DC), and include the file path if available, in the following format: [KG/DC] file_path
- If you don't know the answer, just say so.
- Do not make anything up. Do not include information not provided by the Knowledge Base.
- Addtional user prompt: {user_prompt}

Response:"""

PROMPTS["keywords_extraction"] = """---Role---

You are a helpful assistant tasked with identifying both high-level and low-level keywords in the user's query and conversation history.

---Goal---

Given the query and conversation history, list both high-level and low-level keywords. High-level keywords focus on overarching concepts or themes, while low-level keywords focus on specific entities, details, or concrete terms.

---Instructions---

- Consider both the current query and relevant conversation history when extracting keywords
- Output the keywords in JSON format, it will be parsed by a JSON parser, do not add any extra content in output
- The JSON should have two keys:
  - "high_level_keywords" for overarching concepts or themes
  - "low_level_keywords" for specific entities or details

######################
---Examples---
######################
{examples}

#############################
---Real Data---
######################
Conversation History:
{history}

Current Query: {query}
######################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["keywords_extraction_examples"] = [
    """Example 1:

Query: "How does international trade influence global economic stability?"
################
Output:
{
  "high_level_keywords": ["International trade", "Global economic stability", "Economic impact"],
  "low_level_keywords": ["Trade agreements", "Tariffs", "Currency exchange", "Imports", "Exports"]
}
#############################""",
    """Example 2:

Query: "What are the environmental consequences of deforestation on biodiversity?"
################
Output:
{
  "high_level_keywords": ["Environmental consequences", "Deforestation", "Biodiversity loss"],
  "low_level_keywords": ["Species extinction", "Habitat destruction", "Carbon emissions", "Rainforest", "Ecosystem"]
}
#############################""",
    """Example 3:

Query: "What is the role of education in reducing poverty?"
################
Output:
{
  "high_level_keywords": ["Education", "Poverty reduction", "Socioeconomic development"],
  "low_level_keywords": ["School access", "Literacy rates", "Job training", "Income inequality"]
}
#############################""",
]

PROMPTS["naive_rag_response"] = """---Role---

You are a helpful assistant responding to user query about Document Chunks provided provided in JSON format below.

---Goal---

Generate a concise response based on Document Chunks and follow Response Rules, considering both the conversation history and the current query. Summarize all information in the provided Document Chunks, and incorporating general knowledge relevant to the Document Chunks. Do not include information not provided by Document Chunks.

When handling content with timestamps:
1. Each piece of content has a "created_at" timestamp indicating when we acquired this knowledge
2. When encountering conflicting information, consider both the content and the timestamp
3. Don't automatically prefer the most recent content - use judgment based on the context
4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

---Conversation History---
{history}

---Document Chunks(DC)---
{content_data}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- List up to 5 most important reference sources at the end under "References" section. Clearly indicating each source from Document Chunks(DC), and include the file path if available, in the following format: [DC] file_path
- If you don't know the answer, just say so.
- Do not include information not provided by the Document Chunks.
- Addtional user prompt: {user_prompt}

Response:"""

# TODO: deprecated
PROMPTS[
    "similarity_check"
] = """Please analyze the similarity between these two questions:

Question 1: {original_prompt}
Question 2: {cached_prompt}

Please evaluate whether these two questions are semantically similar, and whether the answer to Question 2 can be used to answer Question 1, provide a similarity score between 0 and 1 directly.

Similarity score criteria:
0: Completely unrelated or answer cannot be reused, including but not limited to:
   - The questions have different topics
   - The locations mentioned in the questions are different
   - The times mentioned in the questions are different
   - The specific individuals mentioned in the questions are different
   - The specific events mentioned in the questions are different
   - The background information in the questions is different
   - The key conditions in the questions are different
1: Identical and answer can be directly reused
0.5: Partially related and answer needs modification to be used
Return only a number between 0-1, without any additional content.
"""
