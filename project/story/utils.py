def split_paragraphs(new_story, num_paragraphs=20):
    paragraphs = new_story.split('。')
    
    paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]
    
    total_paragraphs = len(paragraphs)
    paragraphs_per_section = total_paragraphs // num_paragraphs
    remainder = total_paragraphs % num_paragraphs

    article_list = []

    start = 0
    for i in range(num_paragraphs):
        if i < remainder:
            end = start + paragraphs_per_section + 1
        else:
            end = start + paragraphs_per_section
            
        article_list.append('。'.join(paragraphs[start:end]))
        start = end
    
    # return article_list
    print(article_list)
    for i, paragraph in enumerate(article_list):
        print(f'段落 {i+1}: {paragraph}')



    

a = '''在一個村莊裡，有一個年輕的牧羊男孩負責放牧村民的羊群。他的工作是保護羊群免受狼的攻擊。這位男孩很快感到了無聊，於是他開始用喊叫「狼來了！」來尋求村民的注意。

村民聽到他的呼喊，紛紛前來幫助，但當他們到達時，發現並沒有狼。男孩哈哈大笑，對於自己的惡作劇感到非常高興。

幾天後，男孩再次感到無聊，並再次欺騙村民，喊道：“狼來了！狼來了！”村民再次趕來，但這一次還是沒有發現狼，只有一個嘲笑他們的男孩。

然而，當狼真的出現並威脅到羊群時，男孩急切地大聲呼喊，但這一次村民不再相信他，以為他再次在開玩笑，因此沒有人來救助他。最終，狼襲擊了羊群，男孩無法阻止，導致許多羊被狼吞噬。

這個故事的教訓是告訴人們不要撒謊和欺騙。如果你一再說謊，別人就會失去對你的信任。即使說真話時，也可能因為過去的謊言而失去幫助和支持。因此，這個故事強調了誠實和信任的重要性。
在一個村莊裡，有一個年輕的牧羊男孩負責放牧村民的羊群。他的工作是保護羊群免受狼的攻擊。這位男孩很快感到了無聊，於是他開始用喊叫「狼來了！」來尋求村民的注意。

村民聽到他的呼喊，紛紛前來幫助，但當他們到達時，發現並沒有狼。男孩哈哈大笑，對於自己的惡作劇感到非常高興。

幾天後，男孩再次感到無聊，並再次欺騙村民，喊道：“狼來了！狼來了！”村民再次趕來，但這一次還是沒有發現狼，只有一個嘲笑他們的男孩。

然而，當狼真的出現並威脅到羊群時，男孩急切地大聲呼喊，但這一次村民不再相信他，以為他再次在開玩笑，因此沒有人來救助他。最終，狼襲擊了羊群，男孩無法阻止，導致許多羊被狼吞噬。

這個故事的教訓是告訴人們不要撒謊和欺騙。如果你一再說謊，別人就會失去對你的信任。即使說真話時，也可能因為過去的謊言而失去幫助和支持。因此，這個故事強調了誠實和信任的重要性。'''

split_paragraphs(a)

