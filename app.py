import streamlit as st
import openai
from youtube_transcript_api import YouTubeTranscriptApi
from requests.exceptions import RequestException
key = st.secrets["auth_token"]
# Set up OpenAI API credentials
openai.api_key = key

def combine_transcripts(video_ids):
    combined_text = ""
    for video_id in video_ids:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            for line in transcript:
                combined_text += line['text'] + " "
        except RequestException as e:
            st.error(f"Error retrieving transcript for Video ID: {video_id}")
            st.error(str(e))
    return combined_text

def convert_single_video(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([line['text'] for line in transcript])
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Transorm this into an SEO blog post also make it intuitive inspiring and captivating also make it a little bit on the longer side while maintaining SEO friendliness at the highest level with a title"+ text,
            temperature=0.9,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
        )
        blog_post = response.choices[0].text.strip()
        return blog_post
    except RequestException as e:
        st.error(f"Error converting video with Video ID: {video_id}")
        st.error(str(e))

def about_us():
    st.title('About Us')
    st.write('This is the About Us page.')

def why_choose_us():
    st.title('Why Choose Us')
    st.write('This is the Why Choose Us page.')

def main():
    st.title('GPTTUBE: CONVERT VIDEOS TO HIGH QUALITY SEO BLOG POSTS IN THE BLINK OF AN EYE🚀🚀🚀')

    menu = ['Home', 'About', 'Our Solution', 'Why choose us', 'How to use', 'Limitations']
    choice = st.sidebar.selectbox('Navigation', menu)

    if choice == 'Home':
        st.header('Home')
        option = st.radio('Select an option:', ('Combine Transcripts', 'Convert Single Video'))
        st.write('Do not know what a youtube id means visit #Howtouse to know how!!')
        st.write('Getting an error? Videos of over 15 minutes may not work for transcription check #limitations for more info')
        if option == 'Combine Transcripts':
            st.subheader('Combine Transcripts')
            video_id1 = st.text_input('YouTube Video ID 1')
            video_id2 = st.text_input('YouTube Video ID 2')
            
            if st.button('Combine'):
                video_ids = [video_id1, video_id2]
                combined_text = combine_transcripts(video_ids)
                if combined_text:
                    try:
                        response = openai.Completion.create(
                            engine="text-davinci-003",
                            prompt="Transorm this into an SEO blog post also make it intuitive inspiring and captivating also make it a little bit on the shorter side so that it does not break off while maintaining SEO friendliness at the highest level with a title"+combined_text,
                            temperature=0.9,
                            max_tokens=500,
                            top_p=1.0,
                            frequency_penalty=0.0,
                            presence_penalty=0.6,
                            stop=None,
                        )
                        blog_post = response.choices[0].text.strip()
                        st.markdown('## Combined Blog Post:')
                        st.write(blog_post)
                    except RequestException as e:
                        st.error("Error generating blog post")
                        st.error(str(e))
                else:
                    st.warning("No transcripts found for the provided Video IDs")
                
        elif option == 'Convert Single Video':
            st.subheader('Convert Single Video')
            video_id = st.text_input('YouTube Video ID')
            if st.button('Convert'):
                blog_post = convert_single_video(video_id)
                if blog_post:
                    st.markdown('## Converted Blog Post:')
                    st.write(blog_post)
                else:
                    st.warning("No transcript found for the provided Video ID")

    elif choice == 'About':
                about_us()
    
    elif choice == 'Our Solution':
        our_solution()
    elif choice == 'Why choose us':
        why_choose_us()
    elif choice == 'How to use':
        how()
    elif choice == 'Limitations':
        limit()
def about_us():
    st.title('About Us')
    st.write('GPTTUBE , where we take innovation to a whole new level.🚀🚀🔬🔬')
    st.write('We are a dedicated team of tech enthusiasts and developers, passionate about making the most out of artificial intelligence and its potential to revolutionize content creation.')
    st.write('We began this journey with a simple but groundbreaking idea: to create a bridge between video content and written blogs, powered by advanced AI technology. Our mission is to help content creators, marketers, and businesses maximize their reach and efficiency by converting YouTube videos into engaging, SEO-friendly blog posts.')
    
def our_solution():
    st.title('Our Solution')
    
    st.write('AT GPTTUBE we have developed a robust user friendly platform that harnesses the power of AI to convert your Youtube videos into high quality written content. Our AI model, trained on a massive database of text and videos, understands context, nuances, and language subtleties to provide outputs that maintain the essence and style of your original content')
    st.write('Not only does our platform transcribe the spoken words in your video, but it also analyzes the context and transforms it into well-structured blog posts. Our AI solution even acknowledges the pauses, gestures, and emphasis made in the video to create a post that is not only a transcription but a meaningful narrative that resonates with your audience.')

def why_choose_us():
    st.title('Why Choose Us')
    st.write('In this digital age where content is king, we aim to provide a comprehensive tool that helps you extend your reach and diversify your content. By converting your videos into blog posts, you can cater to various audience preferences, improve your SEO ranking, and ensure a wider presence across different platforms.')
    st.write('We prioritize accuracy, speed, and user experience. With our GPTTUBE , you no longer need to worry about spending hours transcribing videos or hiring costly services. We are here to save you time, resources, and energy so you can focus on what matters most: creating impactful content.')

def how():
    st.write("Quick and easy tutorial to get you up and running🚀🚀")
    st.write('Okay let us say you are new to youtube video ids right?')
    st.write('let us say your url is https://www.youtube.com/watch?v=dQw4w9WgXcQ then your id are the alphabets after the v and the equal sign in some cases there may be an &t=any number then do not copy the letter after the & symbol in this case the id is dQw4w9WgXcQ')
def limit():
    st.title("Although we of course Are OP!! we still sadly have some limitations😔😔 ")
    st.write('1.)Although the GPTTUBE platform works very finely in the 2 transcript combine modes if the videos are a bit too long then it may tend to break off and stop abruptly this feature will be fixed in future updates')
    st.write('2.)Also the model may not accept videos over 15 minute videos(it may or may not based on the amount of words said in the video)')
    st.write('3.)It does not yet transcribe any youtube videos in other languages such as hindi, bengali, spanish etc it also does not work for videos that deny transcription we are working on this issue at the current time by using a video transcription service')
if __name__ == '__main__':
    main()

