---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "3rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false



          
  - block: markdown
    id: notes
    content:
      title: 'Physics Notes'
      subtitle: ''

      text: |-    
        Soon I'll add description of them here.
        Soon I'll add description of them here.
        Soon I'll add description of them [here](/uploads/description-of-notes.pdf).


      
        <h2 id="basic physics notes">Basic Physics Notes</h2>

        
        [mechanics](/uploads/mechanics.pdf)



        <a href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/%E2%96%A0%20basic%20physics/%E2%96%A0%20%20mechanics.pdf" target="_blank">mechanics</a>.</p>
        
        
        <a href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/%E2%96%A0%20basic%20physics/♣%20%20electrodynamics.pdf" target="_blank">electrodynamics</a>.</p>

        

        <h2 id="basic physics notes">Basic Physics Notes</h2>






        <h2 id="Specific physics notes">  Specific physics notes </h2>


        <a href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/☐%20specific%20physics/◊%20cosmology.pdf" target="_blank">cosmology</a>.</p>


        <h2 id="basic physics notes">Notes on Reserach Projects</h2>




    design:
      columns: '1'






---



