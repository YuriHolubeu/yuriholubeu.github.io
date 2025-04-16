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
#   !!!!!!  nbviewer.org обновляет большие файлы по одному дню (альтернатива -  вписывать в код коммит, что неудобно, ибо потом придется менять их)
#
#
#

  
  
  - block: markdown
    id: writing
    content:
      title: <h1>Writing </h1>
      subtitle: ''

      text: |-    

        <p style="line-height: 1;"><font size="3"> 
        In this section, there are my main papers.

        </font></p>

        <div style="line-height: 0.4;"> 


        <ul><li>Master's thesis:  <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/masters_thesis_GF-MTJJ.pdf" target="_blank">Green's Function for Multiterminal Josephson </a> </li> <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/masters_thesis_GF-MTJJ.pdf" target="_blank"> Junctions </a>  </ul> 
        
        
        <ul><li>Bachelor's thesis: <a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/bach_thesis_lensing.pdf" target="_blank">Graviational Lensing of Binary Systems </a></li> </ul>

      
        </div>







    design:
      columns: '1'

  
  - block: markdown
    id: notes
    content:
      title: <h1>Notes on Basic Physics </h1>
      subtitle: ''

      text: |-    

        <p style="line-height: 1;"><font size="3"> 
        For many years I have been studying physics and mathematics using the a philosophy of doing science which I describe <a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/learning physics.pdf" target="_blank">here</a>. In a nutshell, I believe that by structuring information in digital notes and separating the key methods and properties into a dedicated section, one can achieve a deeper understanding. The notes below are an unfinished demo version, which demonstrates how they will look after several years of development. Nevertheless, they contain many methods and many problems for practice with solutions. 
        </font></p>

        <p style="line-height: 1;"><font size="3"> 
        In this section, there are notes on the most important parts of physics. 
        
        </font></p>

        <div style="line-height: 0.4;"> 


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/%E2%96%A0%20%20mechanics.pdf" target="_blank">mechanics</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/◊%20%20field%20theory.pdf" target="_blank">field theory</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/◊%20gravity.pdf" target="_blank">gravity</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/●%20%20quantum%20mechanics.pdf" target="_blank">quantum mechanics</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/◘%20quantum%20field%20theory.pdf" target="_blank">quantum field theory</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☐%20%20statistical%20physics.pdf" target="_blank">statistical physics</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☐ condensed matter p1.pdf" target="_blank">condensed matter part 1</a>, &nbsp; <a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☐ condensed matter p2.pdf" target="_blank">part 2</a> </li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☼%20kinetics.pdf" target="_blank">kinetics</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/♣%20%20electrodynamics.pdf" target="_blank">electrodynamics</a></li></ul>

        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/❀%20continuum%20mechanics.pdf" target="_blank">continuum mechanics</a></li></ul>

        
        </div>













    design:
      columns: '1'
          
  - block: markdown
    id: othernotes
    content:
      title: <h1>Extra Notes</h1>
      subtitle: ''

      text: |-    


        

        <p style="line-height: 1;"><font size="3">   
        From time to time I study mathematics or some specific fields of physics, and below are my notes on some of the most important of them.
          </font></p>



        <table border="0">
        <tr>
        <td><b style="font-size:20px">Notes on Basic Mathematics </b></td>
        <td><b style="font-size:20px">Notes on Specific Physics</b></td>
        </tr>
        <tr>
        <td>
        
        
        <div style="line-height: 0.4;"> 


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/■%20%20mathematical analysis.pdf" target="_blank">mathematical analysis</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/■%20complex analysis.pdf" target="_blank">complex analysis</a></li></ul>

        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◊  differential equations.pdf" target="_blank">differential equations</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◊  partial differential equations.pdf" target="_blank">partial diff. equations</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◊ oscillations.pdf" target="_blank">oscillations</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/■ special functions.pdf" target="_blank">special functions</a></li></ul>

        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/☐  algebra.pdf" target="_blank">algebra</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/☐ linear algebra.pdf" target="_blank">linear algebra</a></li></ul>

        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/♣%20%20probability%20theory.pdf" target="_blank">probability theory</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◘ differential geometry.pdf" target="_blank">differential geometry</a></li></ul>





        </div>





        </td>
        <td>




        <div style="line-height: 0.4;"> 



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/❁%20special%20field%20and%20gravity%20theories.pdf" target="_blank">special field theories</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/◊%20cosmology.pdf" target="_blank">cosmology</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/☐%20thermodynamics.pdf" target="_blank">thermodynamics</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/♣%20magnetism.pdf" target="_blank">magnetism</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/♣%20optics.pdf" target="_blank">optics</a></li></ul>
        


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/☐%20superconductivity.pdf" target="_blank">superconductivity</a></li></ul>
        


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/●%20quantum%20information%20theory.pdf" target="_blank">quantum information</a></li></ul>



        </div>


        
        </td>
        </tr>
        </table>
        
        












          
  - block: markdown
    id: researchnotes
    content:
      title: <h1>Notes on Some Reserach Projects in Physics</h1>
      subtitle: ''
      text: |-
    
        <p style="line-height: 1;"><font size="3"> 
        I had several research projects, which didn't lead to the creation of articles, but I tried my best and made notes on each. One of the projects below is currently my main project.
        </font></p>

        <div style="line-height: 0.4;"> 


        <ul style="margin-bottom: 40px;"><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ spin models with dissipation p1.pdf" target="_blank">spin models with dissipation part 1</a>, &nbsp; <a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ spin models with dissipation p2.pdf" target="_blank">part 2</a> </li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ Green's function special methods.pdf" target="_blank">Green's function special methods for superconductivity</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ sc junctions p1.pdf" target="_blank">superconductive junctions part 1</a>, &nbsp; <a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ sc junctions p2.pdf" target="_blank">part 2</a> </li></ul>


        <ul style="margin-bottom: 40px;"><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/◘%20waveguide%20QED.pdf" target="_blank">waveguide QED</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/◊%20gravitational%20lensing.pdf" target="_blank">gravitational lensing</a></li></ul> 
        
        
        
        
        
        <ul style="margin-bottom: 40px;"><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/◊%20gravitational%20waves.pdf" target="_blank">gravitational waves</a></li></ul>
        


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/❁%20duality%20in%20special%20field%20theories.pdf" target="_blank">duality in special field theories</a></li></ul></li></ul>

        </div>



  - block: markdown
    id: diplomas
    content:
      title: <h1>Diplomas</h1>
      subtitle: ''
      text: |-

        {{< lightbox img1="/media/bd.jpg" caption1="Bachelor's Diploma from MIPT" img2="/media/md.jpg" caption2="Master's Diploma from KU Leuven ⠀⠀⠀⠀(with distinction)" >}}








        



---


