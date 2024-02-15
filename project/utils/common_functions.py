import re
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle_post_request(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            for key, value in data.items():
                request.session[key] = value
            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON format"}, status=400
            )
    return JsonResponse(
        {"status": "error", "message": "Method not allowed"}, status=405
    )

def split_paragraphs(new_story):
    sentences = re.split(r"[。？！；；;]", new_story)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    total_sentences = len(sentences)
    if total_sentences == 0:
        return []
    num_paragraphs = min(total_sentences, 20)
    sentences_per_section = total_sentences // num_paragraphs
    remainder = total_sentences % num_paragraphs
    article_list = []
    start = 0
    for i in range(num_paragraphs):
        if i < remainder:
            end = start + sentences_per_section + 1
        else:
            end = start + sentences_per_section
        paragraph = "。".join(sentences[start:end]) + "。"
        article_list.append(paragraph)
        start = end
    print(article_list)
    return article_list
