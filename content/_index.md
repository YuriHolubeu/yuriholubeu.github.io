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




#
#
#                        !!!!!! не забывай, что я указываю явно номер коммита в гитхабе, что работали пдф файлы. Если обновлял их, то нужно изменить имя коммита тут!!!! Ну или разглдит nbviewer.org
#
#
#

          
  - block: markdown
    id: notes
    content:
      title: <h1>Main Physics Notes</h1>
      subtitle: ''
      text: |-    


        Here are my notes in basic parts of physics, which are most important for a theoretical physicist.
        Soon I'll add description of them <a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/idea-of-notes.pdf" target="_blank">here</a> (?!!!).
        Please, read it, it shows my philosophy and explains, why and how I was working on them.


      
        <h2 id="basic physics notes">Notes on Basic Physics </h2>

        <div style="line-height: 0.4;"> 

        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/%E2%96%A0%20%20mechanics.pdf" target="_blank">mechanics</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/◊%20%20field%20theory.pdf" target="_blank">field theory</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/◊%20%20gravity.pdf" target="_blank">gravity</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/●%20%20quantum%20mechanics.pdf" target="_blank">quantum mechanics</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/◘%20quantum%20field%20theory.pdf" target="_blank">quantum field theory</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/☐%20%20statistical%20physics.pdf" target="_blank">statistical physics</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/☼%20kinetics.pdf" target="_blank">kinetics</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/♣%20%20electrodynamics.pdf" target="_blank">electrodynamics</a></li></ul>

        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/☕%20continuum%20mechanics.pdf" target="_blank">continuum mechanics</a></li></ul>

        
        </div>






    design:
      columns: '1'





          
  - block: markdown
    id: othernotes
    content:
      title: <h1>Extra Notes</h1>
      subtitle: ''

      text: |-    



        From time to time I study mathematics or some specific fields of physics, and here are some notes abot them.

        
        <div style="line-height: 0.4;"> 

        <h2 id="mathematics physics notes">Notes on Basic Mathematics </h2>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/■%20%20mathematical analysis.pdf" target="_blank">mathematical analysis</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/■%20complex analysis.pdf" target="_blank">complex analysis</a></li></ul>

        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◊  differential equations.pdf" target="_blank">differential equations</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◊  partial differential equations.pdf" target="_blank">partial differential equations</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◊ oscillations.pdf" target="_blank">oscillations</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◘ differential geometry.pdf" target="_blank"> differential geometry</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/☐ algebra.pdf" target="_blank">algebra</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/☐ linear algebra.pdf" target="_blank">linear algebra</a></li></ul>

        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/♣%20%20probability%20theory.pdf" target="_blank">probability theory</a></li></ul>




        </div>





        









        <h2 id="Specific physics notes">  Notes on Specific Physics </h2>


        <div style="line-height: 0.4;"> 



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/◊%20cosmology.pdf" target="_blank">cosmology</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/●%20quantum%20information%20theory.pdf" target="_blank">quantum information theory</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/☐%20thermodynamics.pdf" target="_blank">thermodynamics</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/♣%20magnetism.pdf" target="_blank">magnetism</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/optics.pdf" target="_blank">optics</a></li></ul>
        


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/superconductivity.pdf" target="_blank">superconductivity</a></li></ul>
        


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/specific_physics/special%20field%20and%20gravity%20theories.pdf" target="_blank">special field and gravity theories</a></li></ul>
        



        </div>











          
  - block: markdown
    id: researchnotes
    content:
      title: <h1>Notes on Research Projects</h1>
      subtitle: ''
      text: |- 

        <h2 id="basic physics notes">Notes on Some Reserach Projects in Physics</h2>
        

        During past research projects I undrestood many laws of nature and methods, here are notes about them.



        <div style="line-height: 0.4;"> 



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/some%20projects/◊%20gravitational%20lensing.pdf" target="_blank">gravitational lensing</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/some%20projects/◊%20gravitational%20waves.pdf" target="_blank">gravitational waves</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/some%20projects/◘%20waveguide%20QED.pdf" target="_blank">waveguide QED</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/some%20projects/☐%20electronic%20properties%20of%201D%20and%202D%20materials.pdf" target="_blank">electronic properties of 1D and 2D materials</a></li></ul>
        
        
        

        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/6f1f5a4a0005a06918e136b53f5afdfebdd72103/some%20projects/duality%20in%20special%20field%20theories.pdf" target="_blank">duality in special field theories</a></li></ul></li></ul>


        </div>









---


