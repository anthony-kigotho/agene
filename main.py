from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

class ArticleRequest(BaseModel):
    video_ids: list


def fetch_video_transcripts(video_ids):
    transcripts = []
    for video_id in video_ids:
        video_id = video_id
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcripts.append(" ".join([t['text'] for t in transcript]))
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error fetching transcript for {video_id}: {e}")
    return " ".join(transcripts)


@app.post("/generate-article/")
def generate_article_endpoint(request: ArticleRequest):
    video_content = fetch_video_transcripts(request.video_ids)
    return {"article": video_content}

# Example startup instructions
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
