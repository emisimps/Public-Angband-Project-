    
    This changelog summarizes how Part 1 design documents were updated to
    match the final finished product of the Angband Monster File Editor and
    the play-time/timer feature.
    
    1) Monster representation: 
    Original - Monsters were modeled as a set of fields and edits were put in a in-memory structure.
    Final Implementation - Monster is identified as a @dataclass with better fields and categories such as (about/stats/etc..).
    Reasoning - A dataclass makes the model easier to digest, avoids future bugs if there's missing attributes, and makes parsing validation easier.
    
    2) Parsing Responsibility to a Parser Module:
    Original - Parsing was inside a editor class.
    Final Implementation - Parsing was split into a dedicated module. The module had helpers that helped with conversion logic and a parse monster txt function.
    Reasoning - Separating the parser and the UI editor helped the code be maintained easier.
    
    3) Editing Approach:
    Original - Our writing edits could edit the whole monster file, potentially causing corruption.
    Final Implementation - We instead loaded the raw lines of monster txt, we scanned for the monster name, applied edits by adding/replacing specific lines of code, then write the updates.
    Reasoning - Avoids unnecessary harm and lowers the chance of breaking the file structure.
    
    4) Repository added for search and retrieval:
    Original - Search and getting happened directly in the internal list/dictionary.
    Final Implementation - We used a lightweight repository that helped load monsters, support searches by name, helped retrieve the exact information we're looking for.
    Reasoning - Centralized the strategy of looking up logic and keeps the editor/UI simple.
    
    5) Mapping corrections made during development:
    Original - Some keys were represented as hitPoints, armorclass, flagOff which kept the design simple.
    Final Implementation - The storage and parsing is now in sync with the monster txt keys   
    Reasoning - Keeps edits consistent with source data and prevents parsing errors.
    
    6) Edits with validation beforehand
    Original - We assumed user edits were valid.
    Final Implementation - Basic bound and other validation techniques were implemented and fails if the check did not successfully go through.
    Reasoning - Prevents breaking and parsing errors from invalid values.
    
    7) Use Case diagram updated
    Original - Use cases were shown as direct actions.
    Final Implementation - Updated Use Case diagram so the system responsibilities respond to user actions instead of being automated
    Reasoning - The user will start the flow of the game and it simplifies the boundaries.
    
    ## Timer Feature
    - The timer feature is separate from the MFE feature.
    - The final design documents shows which modules store the play-time fields, which write/read them in the savefile, and which UI screens display them.
    - Reason: Keeps gameplay timing logic independent from the monster editor logic.
