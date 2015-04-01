data = {
    'exercise': {
        'template': ['{filename}[project]: {description}'],

        'filename': ['{old_words/template}.py'],

        'description': ['{intro} {requirements}'],

        'intro': ['Using {Module}, {create} a {prog_thing} to {prog_action}.',
            '{Create} a {prog_thing} that {prog_actions}.',
            '{Create} a {prog_thing} such that {prog_actioning} {does} {prog_action}.',
            '{Redo} {former_lab} to {prog_action}.',
            '{Redo} {former_lab} using {prog_things}.'],

        'prog_thing': ['{prog_adj} {prog_thing}', '{prog_adj} {prog_noun}'],
        'prog_things': ['{prog_adj} {prog_things}', '{prog_adj} {prog_nouns}'],
        'prog_adj': ['recursive', 'iterative', 'object-oriented', 'lambda',
            'higher-order', 'first-class', 'obfuscated', 'threaded', 'closed',
            'open', 'volatile', 'elaborate'],
        'prog_noun': ['function', 'class', 'program', 'interface', 'set',
            'list', 'dictionary', 'socket', 'tree', 'race condition'],
        'prog_nouns': ['functions', 'classes', 'programs', 'interfaces', 'sets',
            'lists', 'dictionaries', 'sockets', 'trees', 'race conditions'],
        'prog_verb': ['invert', 'iterate over', 'reduce', 'simplify', 'parse',
            'call', 'return', 'create'],
        'prog_verbs': ['inverts', 'iterates over', 'reduces', 'simplifies',
            'parses', 'calls', 'returns', 'creates'],
        'prog_verbing': ['calling', 'returning'],

        'prog_action': ['{prog_verb} a group of {adjective,prog_adj} {nouns}',
            'repeatedly {math}'],
        'prog_actions': ['{prog_verbs} a group of {adjective,prog_adj} {nouns}',
            'takes in {input} and {prog_actions}'],
        'prog_actioning': ['{prog_verbing} a {prog_thing}',
            '{prog_verbing} {weird_cmd}'],

        'weird_cmd': ['{function}({no_args,args})',
            '{module}.{function}({no_args,args})'],
        'function': ['map', 'reduce', 'sort', 'split', 'filter', 'obfuscate',
            '{old_words/template}', 'load\\_module', 'make', 'compile', 'name'],
        'module': ['{module}.{module}', 'functools', 'math', 'magic',
            'antigravity', 'PIL', 'urllib',
            'sys', 'os', 'random', 'pickle', 're', 'matplotlib'],
        'no_args': [''],
        'args': ['{arg}, {args}', '{arg}', '{args}, {args}', '{arg}={default}'],
        'arg': ['{old_words/template}', '{function}', '{module}', '{prog_adj}',
            '{prog_noun}'],
        'default': ['True', 'False', 'None', '0', '{gen/number}',
            '"{gen/weekday}"'],

        'input': ['a text file', 'a list of {nouns} terminated by {stop}'],

        'stop': ['"stop"', '"cease"', '"terminate"', '"stop now"', '"plzstop"',
            'a null terminator', 'EOF', 'a stop sign',
            'a group of misled parents with their hearts in the right place'],

        'adjective': ['irritated', 'invisible', 'hidden', 'inverted',
            'green', 'volatile', 'sorted'],
        'nouns': ['hamsters', 'toddlers', 'phone numbers', 'sentences',
            'fans', 'text files', 'images', 'calendars', 'cars'],

        'requirements': ['{requirement} {requirements}',
            '{requirement} {requirement}\n{requirements}',
            '{requirement} {requirement} {requirement}',
            '{requirement} {list} {requirements}',
            '{requirement} {table} {requirements}'],
        'requirement': ['Make sure to {technobabble}.',
            'Your program should {technobabble}.',
            'Do not edit the provided {filename}.',
            'Print the result of {prog_actioning}.',
            'Remember to {annoying_busywork}!',
            'You are free to {exercise_freedom}.',
            'You are required to {exercise_freedom}.',
            'When {prog_actioning}, you can {technobabble}.'],

        'list': ['{list_intro}:\nBEGINLIST\n{list_items}\nENDLIST',
            '{list_intro}:\nBEGINENUM\n{list_items}\nENDENUM'],
        'list_intro': ['Make sure to', 'Remember', 'Bear in mind',
            'Additionally', 'You will be graded on how well you'],
        'list_items': ['{list_item}\n{list_item}', '{list_item}\n{list_items}'],
        'list_item': ['LISTITEM. {requirement}'] * 15 + ['LISTITEM. {list}'],

        'table': ['{table_intro}:\n\\\\BEGINTABLE\n{table_header}\n\\midrule\n' +
            '{table_rows}\nENDTABLE\n'],
        'table_intro': ['Take into account',
            'Use the following table for reference'],
        'table_header': ['{old_words/template} & {old_words/template} & ' +
            '{old_words/template}\\\\'],
        'table_rows': ['{table_row}\\\\{table_rows}',
            '{table_row}\\\\{table_row}'],
        'table_row': ['{table_item,old_words/template} & {table_item} & {table_item}\\\\'],
        'table_item': ['{old_words/template}', '${mathbabble}$'],


        'annoying_busywork': ['cite your sources',
            'comment which sections each person wrote',
            'follow {standard_guide} code standards', 'support {old_os}'],
        'exercise_freedom': ['form groups of no more than {gen/number}',
            'form groups of at least {gen/number}', '{technobabble}',
            'reuse code from {former_lab}'],

        'standard_guide': ['PEP-8', 'IEEE', 'ACM', 'GNU', 'Linux',
            'extremely lax'],
        'old_os': ['Windows 98', 'MS-DOS', 'the ENIAC', 'Google Wave'],

        'create': ['write', 'make', 'create'],
        'redo': ['rewrite', 'redo', 'update'],

        'does': ['will'],

        'former_lab': ['{filename} from Lab {gen/number}'],

        'technobabble': ['include the lessons learned in {former_lab}',
            'use {weird_cmd}', 'include support for {prog_things}',
            'catch errors involving {prog_things,nouns}',
            '{predefined_babble}'],
        'predefined_babble': ['avoid Googling "Red Wedding"',
            'appreciate the fleeting experience that is existance',
            'remember to reload, Dr Freeman', 'remember your name',
            'do a good {celebrity} impression', 'stop calling me "Shirley"',
            'tell grandma you love her', 'tip the TAs', 'check the date',
            'lie on the internet', 'wink suggestively', 'bake cookies',
            'experience brief moments of doubt', 'always pay your debts',
            'prepare a romantic candle-lit dinner',
            'appreciate the musical genius that is {musician}',
            'drink Thunder Muscle', 'call missing',
            'avoid eye contact with anyone whose favorite character is Jar-Jar',
            'construct additional pylons', 'eat the last slice of pizza',
            'not trust politicians who resemble famous actors',
            'warn others of the changing seasons',
            'pretend to know sign language',
            'spend way too long on a silly joke'],

        'celebrity': ['Jack Black', 'Morgan Freeman', 'Sir Patrick Stewart',
            'David Cross', 'Richard Stallman', 'Josef Stalin',
            'Richard Stalin', 'Josef Stallman', 'Rosencrantz', 'Guildenstern',
            'GLaDOS'],
        'musician': ['Jack Black', 'Weird Al', 'Ludacris', 'Jonathan Coulton'],

        'math': ['{math_word} ${mathbabble}$'],
        'math_word': ['calculate', 'invert', 'integrate'],
        'mathbabble': ['y = {mathbabble}', 'x^{gen/digit}',
            '{gen/number}^{gen/digit}', '{gen/number}/{gen/number}',
            '{mathbabble} \\cdot {mathbabble}', '{gen/number}_{gen/digit}',
            '{gen/consonant,gen/vowel}_{gen/consonant,gen/vowel}',
            '{mathbabble} ({mathbabble})', '{old_words/template}',
            '{old_words/template} = {mathbabble}', '{mathterm}',
            '{mathterm}({mathbabble})'],
        'mathterm': ['\\lambda', '\\phi', '\\Lambda', '\\Phi', '\\delta',
            '\\Delta', '\\omega', '\\Omega', '\\theta', '\\pi'],
    },

    'old_words' : {
        'template' : ['{old_disease}', '{old_units}', '{old_technology}',
            '{old_science}'],

        #Source: http://en.wikipedia.org/wiki/List_of_deprecated_terms_for_diseases
        'old_disease' : ['apoplexy', 'bilious', 'consumption', 'dropsy',
        'front-street', 'gleet', 'grippe', 'lockjaw', 'norwalk', 'phthisis',
        'quinsy', 'squinsy', 'undulant'],

        #Source: http://en.wikipedia.org/wiki/Category:Obsolete_units_of_measurement
        'old_units' : ['abucco', 'adowlie', 'angula', 'atom', 'bahar', 'buddam',
            'carcel', 'carucate', 'cawnie', 'chungah', 'coomb', 'corgee',
            'cubit', 'cullingey', 'cullishigay', 'delisle', 'dessiatin',
            'dharni', 'dirham', 'ell', 'fanega', 'firlot', 'garce', 'girah',
            'grzywna', 'guz', 'hekat', 'hobbit', 'homer', 'juchart', 'katha',
            'koku', 'kula', 'ligne', 'mache', 'marabba', 'metretes', 'morgen',
            'munjandie', 'oka', 'oxgang', 'peck', 'perch', 'poncelet', 'pood',
            'spat', 'toise', 'unglie', 'wey', 'yojana', 'zentner', 'zolotnik',
            'ordlach'],

        #Source: http://en.wikipedia.org/wiki/Category:Obsolete_technologies
        'old_technology' : ['ballista', 'calculagraph', 'carriage', 'catapult',
            'kinescope', 'mimeograph', 'multi-image', 'pulse-dial', 'rotary',
            'stauroscope', 'sundial'],

        #Source: http://en.wikipedia.org/wiki/Category:Obsolete_scientific_theories
        'old_science' : ['adamic', 'aether', 'antiperistasis', 'barlow',
            'caloric', 'corpuscular', 'cyclol', 'dark-star', 'dualism',
            'enochian', 'etheric', 'firmament', 'galactocentrism', 'geohumoral',
            'vacui', 'imponderable', 'japhetic', 'quasar', 'lescarbault',
            'limbic', 'luminiferous', 'milne', 'phrenol', 'polflucht',
            'recapitulation', 'reticular', 'sublunary', 'impetus',
            'thomson-berthelot', 'troidal', 'trepidation', 'tychonic',
            'vulcan'],

        #Possible other source: http://en.wikipedia.org/wiki/Category:Obsolete_taxonomic_groups, http://en.wikipedia.org/wiki/Category:Modern_obsolete_currencies, http://en.wikipedia.org/wiki/Category:Former_entities
  },
}