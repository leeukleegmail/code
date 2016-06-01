import polib


def translate_file(language='nl'):
    out = polib.POFile()
    out.metadata = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'you@example.com',
    'POT-Creation-Date': '2007-10-18 14:00+0100',
    'PO-Revision-Date': '2007-10-18 14:00+0100',
    'Last-Translator': 'you <you@example.com>',
    'Language-Team': 'English <yourteam@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
    }

    po = polib.pofile('../original.po')
    count = 1
    for entry in po:
        msgid_org = entry.msgid
        if '.' not in entry.msgid:
            name = ''.join(map(lambda x: x if x.islower() else ""+x, entry.msgid))
        else:
            name = ''.join(map(lambda x: x if x.islower() else ""+x, entry.msgid))
            name = name.replace (".", " ")

        while len(name) > 30:
            name = name.split(' ',1)[1]
        name = "%s_translated" % name
        entry_new = polib.POEntry(
        msgid= msgid_org,
        msgstr= name
        )
        out.append(entry_new)
        count +=1

    out.save('nl.po')
    out.save_as_mofile('nl.mo')

    print count

if __name__ == '__main__':
    translate_file()
