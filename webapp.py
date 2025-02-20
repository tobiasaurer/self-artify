import os
import gradio as gr
import self_artify_functions as func


"""
Gradio Interface using Blocks objects.
Further separated into different tabs that include the offered functionalities.
"""


with gr.Blocks(css=".gradio-container {background-image: url('file=https://images.unsplash.com/photo-1545231097-cbd796f1d95f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2190&q=80"
               ) as demo:

    gr.Markdown(
        """
        # Welcome to Self-Artify
        <p align='center'>
        <img src="https://raw.githubusercontent.com/tobiasaurer/self-artify/main/docs/assets/self-artify_logo_small.png"/>
        </p>

        
        ## Choose what you want to be!
        """
    )

    #
    # Avatar Generator Tab
    #
    with gr.Tab("Avatar-Generator"):
        with gr.Row():

            with gr.Column():
                prompt = gr.Textbox(
                    label="Type the gender of your avatar (Optional, e.g. Male, Female)")
                style = gr.Dropdown(
                    choices=func.avatar_styles,
                    label="Select Avatar Character",
                    type="value"
                )

                keep_face = gr.Checkbox(label="Keep the original face in the generated image.")
                delete_input = gr.Checkbox(
                    label="Delete my input image from the server after generating my avatar.")

                input_image = gr.Image(
                    type="filepath",
                    label="Your Image"
                )

                transform_button = gr.Button("Create Avatar")

            with gr.Column():
                transformed_image = gr.Image(label="Avatar")
                transformed_image_path = gr.File(label="Download Avatar")
                delete_button = gr.Button("Delete my avatar from the server")

    transform_button.click(fn=func.avatar_generator,
                           inputs=[prompt, style, input_image, keep_face, delete_input],
                           outputs=[transformed_image, transformed_image_path],
                           queue=True
                           )

    delete_button.click(fn=func.delete_output,
                        inputs=[transformed_image_path],
                        outputs=[])

    #
    # Avatar-Generator Advanced Tab
    #
    with gr.Tab("Avatar-Generator Advanced"):
        with gr.Row():

            with gr.Column():
                prompt = gr.Textbox(label="Prompt")
                keep_face = gr.Checkbox(label="Keep the original face in the generated image.")
                delete_input = gr.Checkbox(
                    label="Delete my input image from the server after generating my avatar.")

                cfg_scale = gr.Slider(minimum=2,
                                      maximum=25,
                                      value=7.5,
                                      step=0.5,
                                      label="CFG-Scale (lower values give the algorithm more freedom")

                strength = gr.Slider(minimum=0.15,
                                     maximum=0.99,
                                     value=0.5,
                                     step=0.025,
                                     label="Strength")

                input_image = gr.Image(
                    type="filepath",
                    label="Your Image"
                )

                transform_button = gr.Button("Create Avatar")

            with gr.Column():
                transformed_image = gr.Image(label="Avatar")
                transformed_image_path = gr.File(label="Download Avatar")
                delete_button = gr.Button("Delete my avatar from the server")

        transform_button.click(fn=func.avatar_generator_advanced,
                               inputs=[prompt, input_image, keep_face,
                                       cfg_scale, strength, delete_input],
                               outputs=[transformed_image, transformed_image_path],
                               queue=True
                               )

        delete_button.click(fn=func.delete_output,
                            inputs=[transformed_image_path],
                            outputs=[])

    #
    # Movie-Poster generator tab
    #
    with gr.Tab("Movie-Poster Generator"):

        with gr.Row():

            with gr.Column():
                movie_title = gr.Textbox(label="Type in a movie title of your choice:")

                poster_style = gr.Dropdown(
                    choices=func.poster_styles,
                    label="Style Picker",
                    type="value"
                )

                generate_poster_button = gr.Button("Generate Unique Movie-Poster")

                poster_path = gr.File(label="Download Poster")

            with gr.Column():
                generated_poster = gr.Image()
                generated_poster.style(
                    height=512,
                    width=384
                )

    generate_poster_button.click(fn=func.poster_generator,
                                 inputs=[movie_title, poster_style],
                                 outputs=[generated_poster, poster_path],
                                 queue=True)


# value of "share" sets whether public link will be created or not
demo.queue(concurrency_count=1)
demo.launch(share=True)
